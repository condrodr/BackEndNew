from EndUser.models import JualanRekomender, RewardList, RewardSpinWheel, Rekomender
from Produk.models import Produk
from Customer.models import RegisteredCustomer
from datetime import date, timedelta
from django.db import transaction
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal, InvalidOperation
from django.db import connection

def _first_day_this_month(today: date) -> date:
    return today.replace(day=1)

def _first_day_last_month(today: date) -> date:
    first_this = _first_day_this_month(today)
    last_prev = first_this - timedelta(days=1)
    return last_prev.replace(day=1)

def _last_day_last_month(today: date) -> date:
    first_this = _first_day_this_month(today)
    return first_this - timedelta(days=1)

def _parse_int_safe(val, default=0):
    try:
        return int(str(val).strip())
    except Exception:
        return default

def _parse_decimal_safe(val, default=Decimal("0")):
    try:
        return Decimal(str(val))
    except (InvalidOperation, TypeError, ValueError):
        return default

def _is_pack_like(kemasan: str) -> bool:
    """
    Anggap 'Dus', 'Pack', 'Karton' sebagai kemasan multipack.
    'Pcs', 'Botol' dianggap unit tunggal.
    """
    if not kemasan:
        return False
    k = kemasan.strip().lower()
    return k in {"dus", "pack", "karton", "box", "dus/box"}

@api_view(["POST"])
def summary_rekomender(request):
    """
    Body JSON:
    {
      "id_rekomender": "RKM-001"
    }
    """
    id_rekom = request.data.get("id_rekomender")
    if not id_rekom:
        return Response({"error": "id_rekomender is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Data rekomender
    rekom = Rekomender.objects.filter(id_rekomender=id_rekom).first()
    if not rekom:
        return Response({"error": f"Rekomender {id_rekom} tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)

    budget_per_liter = int(rekom.budget_per_liter or 0)

    # Range tanggal
    today = timezone.localdate()
    first_this = _first_day_this_month(today)
    first_prev = _first_day_last_month(today)
    last_prev = _last_day_last_month(today)

    # Query transaksi
    base_qs = JualanRekomender.objects.filter(id_rekomender=id_rekom)
    qs_bulan_ini = base_qs.filter(tanggal__gte=first_this, tanggal__lte=today) \
                          .values("produk_dijual", "jumlah_produk", "kemasan_produk", "tanggal", "dms_rekomender")
    qs_bulan_lalu = base_qs.filter(tanggal__gte=first_prev, tanggal__lte=last_prev) \
                           .values("produk_dijual", "jumlah_produk", "kemasan_produk", "tanggal", "dms_rekomender")

    # Siapkan peta produk (lookup sekali)
    produk_names = set([r["produk_dijual"] for r in qs_bulan_ini] + [r["produk_dijual"] for r in qs_bulan_lalu])
    produk_map = {
        p["nama_produk"]: p
        for p in Produk.objects.filter(nama_produk__in=produk_names).values("nama_produk", "isi_per_pack", "volume_per_pcs")
    }

    def hitung_liter(qs_values):
        total_liter = Decimal("0")
        trx = 0
        breakdown = {}

        for row in qs_values:

            nama_barang = row["produk_dijual"]
            
            kemasan = row.get("kemasan_produk") or ""
            print(kemasan)
            qty = _parse_int_safe(row["jumlah_produk"], 0)

            prod = produk_map.get(nama_barang)
            tanggal = row["tanggal"]
            nama_outlet = (
                RegisteredCustomer.objects.filter(kode_prinsipal_outlet=row["dms_rekomender"])
                .values_list("nama_outlet", flat=True)
                .first()
            )
            if not prod:
                # Produk tak ditemukan di master -> skip
                continue

            isi_per_pack = _parse_int_safe(prod.get("isi_per_pack"), 1)
            vol_unit = _parse_decimal_safe(prod.get("volume_per_pcs"), Decimal("0"))  # liter per unit
            print(isi_per_pack)
            # Faktor kemasan
            if _is_pack_like(kemasan):
                faktor = isi_per_pack
            else:
                faktor = 1

            liter = Decimal(qty) * Decimal(faktor) * vol_unit

            total_liter += liter
            trx += 1

            bd = breakdown.get(nama_barang) or {
                "produk": nama_barang,
                "jumlah_produk": qty,
                "liter": Decimal("0"),
                "kemasan_produk": kemasan,
                "tanggal" : tanggal,
                "nama_outlet": nama_outlet

            }
            bd["liter"] += liter
            breakdown[nama_barang] = bd

        # konversi Decimal ke float untuk JSON
        out = []
        for v in breakdown.values():
            out.append({
                "produk": v["produk"],
                "jumlah_produk": qty,
                "kemasan_produk": kemasan,
                "liter": float(v["liter"]),
                "tanggal" : tanggal,
                "nama_outlet" : nama_outlet
              
            })
        return float(total_liter), trx, out

    liter_bln_ini, trx_bln_ini, breakdown_bln_ini = hitung_liter(qs_bulan_ini)
    liter_bln_lalu, trx_bln_lalu, breakdown_bln_lalu = hitung_liter(qs_bulan_lalu)

    budget_bln_ini = int(round(liter_bln_ini * budget_per_liter))
    budget_bln_lalu = int(round(liter_bln_lalu * budget_per_liter))

    data = {
        "rekomender": {
            "id_rekomender": rekom.id_rekomender,
            "nama_rekomender": rekom.nama_rekomender,
            "kode_outlet": rekom.kode_outlet,
            "dms_rekomender": rekom.dms_rekomender,
            "budget_per_liter": budget_per_liter,
        },
        "periode": {
            "bulan_ini": {"tanggal_awal": str(first_this), "tanggal_akhir": str(today)},
            "bulan_lalu": {"tanggal_awal": str(first_prev), "tanggal_akhir": str(last_prev)},
        },
        "ringkasan": {
            "liter_bulan_ini": round(liter_bln_ini, 2),
            "liter_bulan_lalu": round(liter_bln_lalu, 2),
            "budget_terpakai_bulan_ini": budget_bln_ini,
            "budget_terpakai_bulan_lalu": budget_bln_lalu,
            "transaksi_bulan_ini": trx_bln_ini,
            "transaksi_bulan_lalu": trx_bln_lalu,
        },
        "breakdown": {
            "bulan_ini": breakdown_bln_ini,
            "bulan_lalu": breakdown_bln_lalu,
        },
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def summary_outlet(request):
    dms_rekomender = request.data.get('dms_rekomender')
    if dms_rekomender is None:
        return Response({'error': 'dms_rekomender is required'}, status=400)

    with connection.cursor() as cursor:
        cursor.execute("""
                       
          SELECT
               
               
               SUM(CASE WHEN  p.kemasan_produk = 'Dus' AND p.merek_produk = 'Enduro' AND jr.tanggal BETWEEN date('now','start of month') AND date('now')
                    THEN p.volume_per_pcs *
                       (CASE WHEN jr.kemasan_produk = 'Dus'
                        THEN jr.jumlah_produk * p.isi_per_pack
                        ELSE jr.jumlah_produk END)
                    ELSE 0 END) as liter_enduro,
               SUM(CASE WHEN  p.kemasan_produk = 'Dus' AND p.merek_produk = 'Enduro' AND jr.tanggal BETWEEN date('now','start of month','-1 month') AND date('now','start of month','-1 day')
                    THEN p.volume_per_pcs *
                       (CASE WHEN jr.kemasan_produk = 'Dus'
                        THEN jr.jumlah_produk * p.isi_per_pack
                        ELSE jr.jumlah_produk END)
                    ELSE 0 END) as liter_enduro_lalu,
               SUM(CASE WHEN p.kemasan_produk = 'Dus' AND p.merek_produk = 'Fastron' AND jr.tanggal BETWEEN date('now','start of month') AND date('now')
                    THEN p.volume_per_pcs *
                       (CASE WHEN jr.kemasan_produk = 'Dus'
                        THEN jr.jumlah_produk * p.isi_per_pack
                        ELSE jr.jumlah_produk END)
                    ELSE 0 END) as liter_fastron,
              
               SUM(CASE WHEN  p.kemasan_produk = 'Dus' AND p.merek_produk = 'Fastron' AND jr.tanggal BETWEEN date('now','start of month','-1 month') AND date('now','start of month','-1 day')
                    THEN p.volume_per_pcs *
                       (CASE WHEN jr.kemasan_produk = 'Dus'
                        THEN jr.jumlah_produk * p.isi_per_pack
                        ELSE jr.jumlah_produk END)
                    ELSE 0 END) as liter_fastron_lalu,
               SUM(CASE WHEN p.kemasan_produk = 'Dus' AND jr.tanggal BETWEEN date('now','start of month') AND date('now')
                    THEN p.volume_per_pcs *
                       (CASE WHEN jr.kemasan_produk = 'Dus'
                        THEN jr.jumlah_produk * p.isi_per_pack
                        ELSE jr.jumlah_produk END)
                    ELSE 0 END) as liter_total,
               SUM(CASE WHEN  p.kemasan_produk = 'Dus' AND jr.tanggal BETWEEN date('now','start of month','-1 month') AND date('now','start of month','-1 day')
                    THEN p.volume_per_pcs *
                       (CASE WHEN jr.kemasan_produk = 'Dus'
                        THEN jr.jumlah_produk * p.isi_per_pack
                        ELSE jr.jumlah_produk END)
                    ELSE 0 END) as liter_total_lalu
              
          FROM
               
               "EndUser_jualanrekomender" as jr 
               
               INNER JOIN "Produk_produk" as p ON p.nama_produk = jr.produk_dijual
          WHERE
               jr.dms_rekomender = %s
          """, [dms_rekomender])
        
        row = cursor.fetchone()
        
        (liter_enduro, liter_enduro_lalu, liter_fastron, liter_fastron_lalu, liter_total, liter_total_lalu   )= row  
        
        cust = RegisteredCustomer.objects.get(kode_prinsipal_outlet=dms_rekomender)

        nama_outlet = cust.nama_outlet
        rekomender = Rekomender.objects.get(dms_rekomender=dms_rekomender)
        budget = rekomender.budget_per_liter
        budget_klaim_reward = budget * liter_total
        budget_klaim_reward_lalu = budget * liter_total_lalu

        
     
        con = {
            'nama_outlet':nama_outlet,
            'budget_klaim_reward':budget_klaim_reward,
            'budget_klaim_reward_lalu':budget_klaim_reward_lalu,
            'liter_total':liter_total,
            'liter_total_lalu':liter_total_lalu,
            'liter_enduro':liter_enduro,
            'liter_enduro_lalu':liter_enduro_lalu,
            'liter_fastron':liter_fastron,
            'liter_fastron_lalu':liter_fastron_lalu,
        }

        return Response(con)
    


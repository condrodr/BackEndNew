from rest_framework import serializers
from Driver.models import Driver, UpdateNotaKirimSebagian, DetailSisaNotaTerkirimSebagian, PlanKiriman, DetailPlanKiriman

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            'id',
            'no_kendaraan',
            'nama_supir',
            'no_telepon_supir',
            'jenis_kendaraan',
            'merek_kendaraan',
            'status_kendaraan'
        )

class PlanKirimanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanKiriman
        fields = (
            'id',
            'no_kendaraan',
            'id_plan_kiriman',
            'nomer_urut_kiriman',
            'nama_supir',
            'tanggal_kiriman',
            'total_jarak_km',
            'biaya_kiriman',
            'start_kerja',
            'selesai_kerja',
            'ada_returan',
            'keterangan_retur'
        )

class DetailPlanKirimanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPlanKiriman
        fields = (
            'id',
            'no_nota_keluar',
            'no_sj_keluar',
            'jenis_transaksi',
            'nama_tujuan_kiriman',
            'GPS_lokasi_kiriman',
            'no_urut_kiriman',
            'id_plan_kiriman',
            'id_detail_plan_kiriman'
        )

class UpdateNotaKirimSebagianSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateNotaKirimSebagian
        fields = (
            'id',
            'tujuan_kirim',
            'no_nota_keluar',
            'nilai_belum_terkirim',
            'terakhir_terkirim',
            'status_kiriman',
            'id_nota_sebagian'
        )

class DetailSisaNotaTerkirimSebagianSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSisaNotaTerkirimSebagian
        fields = (
            'id',
            'no_nota_keluar',
            'id_detail_nota',
            'id_nota_sebagian',
            'tujuan_kirim',
            'nama_produk',
            'kemasan_produk',
            'jumlah_produk',
            'harga_jual_pcs',
            'discount_produk',
            'subtotal_vol',
            'jumlah_order_terkirim' 
        )
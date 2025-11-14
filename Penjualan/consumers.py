import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Sum
from asgiref.sync import sync_to_async


class ProdukKeluarConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("🔗 WebSocket Terhubung!")
        await self.accept()

    async def receive(self, text_data):
        from .models import DetailPenjualan  # ✅ Import model di dalam fungsi

        print(f"📩 Menerima data: {text_data}")

        try:
            data = json.loads(text_data)

            if "produk_keluar" in data:
                produk_keluar = data["produk_keluar"]
                no_nota_jual = data.get("no_nota_jual")

                hasil_perhitungan = []
                for item in produk_keluar:
                    nama_produk = item["nama_produk"]
                    jumlah_keluar = item["jumlah_order"]
                    harga_per_unit = item["harga_jual_pcs"]

                    # ✅ Gunakan `sync_to_async` agar query tidak error
                    total_order = await sync_to_async(self.get_total_terkirim)(nama_produk, no_nota_jual)

                    jumlah_belum_terkirim = max(0, total_order - jumlah_keluar )
                    
                    nilai_belum_terkirim = jumlah_belum_terkirim * harga_per_unit

                    hasil_perhitungan.append({
                        "nama_produk": nama_produk,
                        "jumlah_keluar": jumlah_keluar,
                        "total_order": total_order,
                        "jumlah_belum_terkirim": jumlah_belum_terkirim,
                        "nilai_belum_terkirim": nilai_belum_terkirim
                    })

                print(f"📤 Mengirim Data ke Client: {hasil_perhitungan}")
                await self.send(text_data=json.dumps(hasil_perhitungan))

        except Exception as e:
            print(f"❌ Error: {e}")
            await self.send(text_data=json.dumps({"error": str(e)}))

    # ✅ Fungsi ini dijalankan dalam `sync_to_async`
    def get_total_terkirim(self, nama_produk, no_nota_jual):
        from .models import DetailPenjualan
        return DetailPenjualan.objects.filter(nama_produk=nama_produk, no_nota_jual=no_nota_jual).aggregate(
            total=Sum("jumlah_order")
        )["total"] or 0

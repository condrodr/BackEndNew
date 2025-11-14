from django.contrib import admin
from .models import StokUtama, SelisihBongkarMuat, KartuStok, StokTransit
# Register your models here.
class StokUtamaAdmin(admin.ModelAdmin):
    list_display = [
        'nama_produk',
        'kode_produk',
        'jumlah_barang',
        'gudang_cabang',
        
        
       

    ]
    list_filter = ('gudang_cabang','nama_produk')
    search_fields = ('nama_produk','produsen_produk')

admin.site.register(StokUtama, StokUtamaAdmin)
admin.site.register( SelisihBongkarMuat)
class KartuStokAdmin(admin.ModelAdmin):
    list_display = [
        'nama_produk',
        'kode_produk',
        'gudang_cabang',
        'detail_lokasi',
        'stok_awal',
        'stok_akhir'
        
        
       

    ]
    list_filter = ('gudang_cabang','nama_produk','detail_lokasi')
    search_fields = ('nama_produk','detail_lokasi')

admin.site.register( KartuStok,KartuStokAdmin)
admin.site.register( StokTransit)
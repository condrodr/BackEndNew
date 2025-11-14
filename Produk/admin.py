from django.contrib import admin
from .models import Produk
# Register your models here.
class ProdukAdmin(admin.ModelAdmin):
    list_display = [
        'nama_produk',
        'alias_produk',
        'produsen_produk',
        'kode_produk',
        'kimap_produk',
        'submerek_produk',
        'kemasan_produk',
        'isi_per_pack',
        'volume_per_pcs',
        'deskripsi_produk',
        'harga_HTO_pcs',
        'harga_HET_pcs',
        'divisi_kantor',
       

    ]
    list_filter = ('kategori_produk','produsen_produk','merek_produk','submerek_produk')
    search_fields = ('nama_produk','produsen_produk')
  

admin.site.register(Produk, ProdukAdmin)
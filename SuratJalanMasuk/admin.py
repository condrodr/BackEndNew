from django.contrib import admin
from .models import SJMasuk, DetailSJMasuk
# Register your models here.
class SJMasukAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'no_SJ_masuk',
            'no_nota_masuk',
            'no_kendaraan',
            'nama_pembawa',
            'asal_kiriman',
            'timestamp',
            'gudang_cabang',
            'nama_penerima',
            'jenis_sj_masuk',
            'modal_SJ_masuk',

    ]
    
    search_fields = ('no_nota_masuk','no_SJ_masuk')
  
admin.site.register(SJMasuk,SJMasukAdmin)

class DetailSJMasukAdmin(admin.ModelAdmin):
    list_display = [
            'id_detailSJM',
            'no_SJ_masuk',
            'no_nota_masuk',
            'id_detail_nota_masuk',
            'nama_produk',
            'kode_produk',
            'jumlah_order',
            'kemasan_produk',
            'asal_kiriman',
            'jenis_sj_masuk',
            'timestamp',
            'harga_beli_pcs',

    ]
    
    search_fields = ('no_nota_masuk','no_SJ_masuk','nama_produk')
admin.site.register(DetailSJMasuk,DetailSJMasukAdmin)
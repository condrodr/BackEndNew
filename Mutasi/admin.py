from django.contrib import admin
from Mutasi.models import NotaMutasiKeluarCart, TerimaMutasiCart, DetailMutasiKeluarCart

# Register your models here.

class NotaMutasiKeluarAdmin(admin.ModelAdmin):
    list_display = [
            'no_mutasi',
            'gudang_awal',
            'tujuan_kirim',
            'tanggal_mutasi',
            'jenis_mutasi',
            'status_kiriman',
            'keterangan_mutasi',
    ]
    
    search_fields = ('no_mutasi','gudang_awal')

admin.site.register(NotaMutasiKeluarCart, NotaMutasiKeluarAdmin)

class TerimaMutasiCartAdmin(admin.ModelAdmin):
    list_display = [
            'no_mutasi',
            'jenis_mutasi',
            'tanggal_diterima',
            'status_penerimaan',
            'keterangan_penerimaan',
    ]
    
    search_fields = ('no_mutasi',)
admin.site.register(TerimaMutasiCart, TerimaMutasiCartAdmin)

class DetailMutasiKeluarCartAdmin(admin.ModelAdmin):
    list_display = [
            'no_mutasi',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order',
            'tanggal_mutasi',
            'id_detail_mutasi',
            'harga_modal_pcs',
            
            
    ]
    
    search_fields = ('no_mutasi','nama_produk')
admin.site.register(DetailMutasiKeluarCart,DetailMutasiKeluarCartAdmin)
from django.contrib import admin
from .models import NotaPembelian,DetailPembelian
# Register your models here.
class NotaPembelianAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'no_nota_beli',
            'supplier',
            'gudang_cabang',
            'faktur_atau_tidak',
            'hutang_standing',
            'diorder_oleh',
            'nilai_nota_beli',
            'tanggal_nota_beli',
            'jatuh_tempo_beli',
            'status_nota_beli',
            'status_barang_beli',
            'divisi_kantor',
            'perusahaan_kantor',
            'total_volume_nota',
            'cluster_pembeli',

    ]
    
    search_fields = ('gudang_cabang','no_nota_beli')
admin.site.register(NotaPembelian,NotaPembelianAdmin)
class DetailPembelianAdmin(admin.ModelAdmin):
    list_display = [
            'id_detail_nota_masuk',
            'no_nota_beli',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order_beli',
            'harga_beli_pcs',
            'kantor_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
            'supplier'

    ]
    
    search_fields = ('nama_produk','no_nota_beli','id_detail_nota_masuk')
admin.site.register(DetailPembelian,DetailPembelianAdmin)

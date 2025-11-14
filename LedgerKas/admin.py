from django.contrib import admin
from .models import Kas, JournalEntry, JournalEntryLine
# Register your models here.
class KasAdmin(admin.ModelAdmin):
    list_display = [
            'tanggal_kas',
            'keluar_masuk',
            'bentuk_kas',
            'detail_kas',
            'jenis_transaksi',
            'keterangan_transaksi',
            'nilai_transaksi',
            'transaction_id',
    ]
    
    search_fields = ('detail_kas','keluar_masuk')

admin.site.register(Kas, KasAdmin)

class JournalEntryAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'kategori_action',
            'detaildeskripsi',
            'timestamp',
            'kode_entry',
            'validitas'
    ]
    
    search_fields = ('kategori_action','kode_entry')

admin.site.register(JournalEntry, JournalEntryAdmin)

class JournalEntryLineAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'kode_entry',
            'nama_akun',
            'kode_akun',
            'date',
            'tipe_journal',
            'value_transaksi'
    ]
    
    search_fields = ('kode_entry','kode_akun')

admin.site.register(JournalEntryLine, JournalEntryLineAdmin)
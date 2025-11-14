from django.contrib import admin
from .models import NotaPenjualan, DetailPenjualan
# Register your models here.

class NotaPenjualanAdmin(admin.ModelAdmin):
    list_display = [
        'id',
            'nama_outlet',
            'no_nota_jual',
            'jenis_penjualan',
            'nilai_nota_jual',
            'piutang_standing',
            'kantor_cabang',
            'nama_salesman',
            'status_nota',
            'status_barang',
            'tanggal_nota',
            'jatuh_tempo_nota',
            'divisi_kantor',
            'perusahaan_kantor',
       

    ]
    list_filter = ('kantor_cabang','perusahaan_kantor','divisi_kantor')
    search_fields = ('nama_outlet','no_nota_jual')
admin.site.register(NotaPenjualan,NotaPenjualanAdmin)

class DetailPenjualanAdmin(admin.ModelAdmin):
    list_display = [
        'id',
            'no_nota_jual',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order',
            'harga_jual_pcs',
            'discount_produk',
            
            'subtotal_vol',
            'tanggal_nota',
       

    ]
    # list_filter = ('kantor_cabang','perusahaan_kantor','divisi_kantor')
    search_fields = ('no_nota_jual','nama_produk')

admin.site.register(DetailPenjualan, DetailPenjualanAdmin)


# AkunPembukuan (models.model)
# nama_akun
# kode_akun
# tipe_akun = choice (Aset, Hutang, Modal, Pendapatan, Pengeluaran)

# JournalEntry (models.model)
# deskripsi =
# timestamp = 
# kode_entry = 
# validitas = unfinished (jika journal entry line belum ada), valid (jika debit di journalentryline sama dengan credit) or invalid (kalau credit debit tidak setara)

# JournalEntryLine (models.model)
# kode_entry =
# nama_akun =
# kode_akun =
# date = 
# tipe_journal = debit/credit
# Value_transaksi = integer

# Rencana pembuatan Transaksi Cash Sistem
# 1. Ada halaman buat bikin akun accounting (ini pengkodean akunting yang dipakai mba tanti dibuat oleh akuntan publik yg audit GPP)
# 2. ⁠Halaman Pengeluaran Biaya -  buat Journal Entry - Deskripsi (Biaya Kirim ke Agung Mulyo) -> next detail line (mirip kayak bikin nota) -> isi debit (pilih akun biaya ) lalu (nilai biaya) dikeluarkan dari (pilih akun cash jogja/bank bca/cash cilacap etc) 
# 3. ⁠Halaman Penerimaan Uang Masuk kebalikannya
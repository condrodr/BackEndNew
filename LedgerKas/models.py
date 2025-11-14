from django.db import models
from BackEndNew import choice as c

# Create your models here.
class Kas(models.Model):
    tanggal_kas = models.DateField(auto_now=False,null=True,blank=True) #ini adalah tanggal kapan uang keluar atau masuk
    keluar_masuk = models.CharField(max_length=200,blank=True,null=True) # ini menjelaskan uang masuk/keluar/pembayaran supplier/pembelian asset,penarikan modal, pembayaran piutang lain2. (pending =  BG)
    bentuk_kas = models.CharField(max_length=200,blank=True,null=True) # ini adalah bentuk uang bank_mandiri/bank_bca/kas
    detail_kas = models.CharField(max_length=200,blank=True,null=True) # ini adalah detail lokasi uang no_rekening/kantor_pemegang
    jenis_transaksi = models.CharField(max_length=200,blank=True,null=True) # ini adalah jenis transaksi biaya/pelanggan bayar/kita bayar/pendapatan lain-lain, tambahan pinjaman, penjualan asset
    detail_transaksi = models.CharField(max_length=200,blank=True,null=True) # ini adalah detail transaksi no nota jual/no nota beli/kode_biaya(diketik)
    keterangan_transaksi = models.CharField(max_length=200,blank=True,null=True) # ini adalah keterangan transaksi seperti Ada lunas sama cicilan, pendapatan lain2(ketik), jika bg(sudah cair/belum cair)
    nilai_transaksi = models.IntegerField(null=True,blank=True,default=0)
    transaction_id = models.CharField(max_length=200,blank=True,null=True) # ini adalah kode unik untuk memanggil ulang transaksi ini
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    kantor_cabang = models.CharField(max_length=200,blank=True,null=True)
    #2 hal dibawah ini untuk mentracking kebohongan
    transaction_user = models.CharField(max_length=200,blank=True,null=True) #Tracking siapa yang bohong
    timestamp = models.DateTimeField(auto_now=True)

class MasterAkun(models.Model):
####Data Pembuatan Akun Accounting:######
    kode_akun = models.CharField(max_length=200,blank=True,null=True) # awali dengan 1 untuk asset, 2 untuk hutang, 3 untuk equity, 4 untuk revenue dan 5 untuk expenses
    nama_akun = models.CharField(max_length=200,blank=True,null=True) # beri nama akun secara jelas seperti - kas di cabang cilacap, bank mandiri 139-00-09064423
    kategori = models.CharField(max_length=200,blank=True,null=True) # ini adalah kategori dalam accounting seperti asset, hutang, equity, revenue, expenses
    sub_kategori = models.CharField(max_length=200,blank=True,null=True) # ini adalah detail dari kategori seperti inventory, kas, equipment
    keterangan = models.CharField(max_length=200,blank=True,null=True) # ini adalah penjelasan terkait akun yang dibuat detailnya akun apa ini

# class TabelNeracaAwal(models.Model):
# ####Data Neraca awal Accounting Accounting: selalu gunakan yang terbaru tidak perlu direplace###### 
#     kode_akun = models.CharField(max_length=200,blank=True,null=True) 
#     nama_akun = models.CharField(max_length=200,blank=True,null=True) 
#     kategori = models.CharField(max_length=200,blank=True,null=True)
#     jenis_data = models.CharField(max_length=200,blank=True,null=True) # ini untuk membedakan ini adata neraca awal, atau PNL awal atau sejenis
#     saldo_awal = models.IntegerField(null=True,blank=True) # ini adalah nominal saldo awal
#     timestamp = models.DateTimeField(auto_now=False,blank=True,null=True) # ini adalah waktu dari cut off data ini dibuat


# class JurnalEntry(models.Model):
# ####Data Pembuatan Journal Entry Accounting:######
#     timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)
#     keterangan = models.CharField(max_length=200,blank=True,null=True)
#     debit_kredit = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_debit_kredit)
#     nama_akun = models.CharField(max_length=200,blank=True,null=True)
#     kode_akun = models.CharField(max_length=200,blank=True,null=True)
#     kategori = models.CharField(max_length=200,blank=True,null=True)
#     sub_kategori = models.CharField(max_length=200,blank=True,null=True)
#     nominal = models.IntegerField(null=True,blank=True)
#     kode_transaksi = models.CharField(max_length=200,blank=True,null=True) # kode transaksi digunakan untuk merefer transaksi


class JournalEntry(models.Model):
   # deskripsi = models.CharField(max_length=200,blank=True,null=True)
    kategori_action = models.CharField(max_length=200,blank=True,null=True)
    detaildeskripsi = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateField(auto_now=True,blank=True,null=True)
    kode_entry =  models.CharField(max_length=200,blank=True,null=True)
    validitas =  models.CharField(max_length=200,blank=True,null=True)


class JournalEntryLine(models.Model):
    kode_entry =  models.CharField(max_length=200,blank=True,null=True)
    nama_akun =  models.CharField(max_length=200,blank=True,null=True)
    kode_akun =  models.CharField(max_length=200,blank=True,null=True)
    date = models.DateField(auto_now=False,blank=True,null=True)
    tipe_journal = models.CharField(max_length=200,blank=True,null=True)
    value_transaksi = models.CharField(max_length=200,blank=True,null=True)




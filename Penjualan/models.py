from django.db import models
from BackEndNew import choice as c

# Create your models here.
class NotaPenjualan(models.Model):
    nama_outlet = models.CharField(max_length=200,blank=True,null=True)
    kode_outlet = models.CharField(max_length=200,blank=True,null=True) #kita akan pivot data konsumen menggunakan ini
    no_nota_jual = models.CharField(max_length=200,blank=True,null=True)
    jenis_penjualan = models.CharField(max_length=200,blank=True,null=True,default='offline',choices=c.choice_jenis_penjualan) #penjualan offline/power/tokopedia/blibli/shoppee
    jenis_faktur = models.CharField(max_length=200,blank=True,null=True,default='tanpa faktur',choices=c.choice_faktur) #faktur tidak print, print faktur, online request gunggung, offline request gunggung - denda 2% 
    nilai_nota_jual = models.IntegerField(null=True,blank=True,default=0)
    piutang_standing = models.IntegerField(null=True,blank=True,default=0)
    kantor_cabang = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_kantor)
    nama_salesman = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_nama_salesman)
    status_nota = models.CharField(max_length=200,default='belum lunas',blank=True,null=True)
    status_barang = models.CharField(max_length=200,default='belum dikirim',blank=True,null=True)#belum dikirim = jumlah order terikirim adalah 0, terkirim sebagian = jumlah order terkirim lebih dari 0, terkirim = jumlah order terkirim sama dengan total jumlah_order
    tanggal_nota = models.DateField(auto_now=False,blank=True,null=True)
    jatuh_tempo_nota = models.DateField(auto_now=False,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_divisi_kantor)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_perusahaan_kantor)
    ikut_program_apa = models.CharField(max_length=200,blank=True,null=True,default='tidak ikut') #ini adalah keterangan ikut program flashsale (produk) non kontrak apa transaksi pada nota ini
    catatan_tambahan = models.CharField(max_length=200,blank=True,null=True) #ini adalah jika admin / sales mau memberi catatan pada nota

class DetailPenjualan(models.Model):
    no_nota_jual = models.CharField(max_length=200,blank=True,null=True)
    id_detail_nota_jual = models.CharField(max_length=200,blank=True,null=True)
    kode_outlet = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_order = models.IntegerField(blank=True,null=True)
    harga_jual_pcs = models.IntegerField(blank=True,null=True)
    discount_produk = models.FloatField(blank=True,null=True)
    subtotal_vol = models.FloatField(blank=True,null=True)
    jumlah_order_terkirim = models.IntegerField(blank=True,null=True)
    tanggal_nota = models.DateField(auto_now=False,blank=True,null=True)

class PendingNotaPenjualan(models.Model):
    nama_outlet = models.CharField(max_length=200,blank=True,null=True)
    kode_outlet = models.CharField(max_length=200,blank=True,null=True)
    no_nota_jual = models.CharField(max_length=200,blank=True,null=True)
    jenis_penjualan = models.CharField(max_length=200,blank=True,null=True,default='offline',choices=c.choice_jenis_penjualan)
    jenis_faktur = models.BooleanField(blank=False,null=False)
    nilai_nota_jual = models.IntegerField(null=True,blank=True,default=0)
    nama_salesman = models.CharField(max_length=200,blank=True,null=True)
    tanggal_nota = models.DateField(auto_now=False,blank=True,null=True)
    jatuh_tempo_nota = models.DateField(auto_now=False,blank=True,null=True)
    kantor_cabang = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_kantor)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True,default='Pelumas',choices=c.choice_divisi_kantor)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True,default='PT. Gelora Putra Perkasa',choices=c.choice_perusahaan_kantor)

class PendingDetailPenjualan(models.Model):
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_order = models.IntegerField(blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    discount_produk = models.FloatField(blank=True,null=True)
    no_nota_jual = models.CharField(max_length=200,blank=True,null=True)
    harga_jual_pcs = models.IntegerField(blank=True,null=True)
    kantor_cabang = models.CharField(max_length=200,blank=True,null=True,default="Cilacap")
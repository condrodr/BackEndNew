from django.db import models

# Create your models here.
class SJMasuk(models.Model):
    no_SJ_masuk = models.CharField(max_length=200,blank=True,null=True)
    no_nota_masuk = models.CharField(max_length=200,blank=True,null=True)
    no_kendaraan = models.CharField(max_length=200,blank=True,null=True) # no kendaraan yang membawa kiriman
    nama_pembawa = models.CharField(max_length=200,blank=True,null=True) # nama supir yang membawa produk
    asal_kiriman = models.CharField(max_length=200,blank=True,null=True) # asal perusahaan atau tempat barang ini dikirim dari
    timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    nama_penerima = models.CharField(max_length=200,blank=True,null=True)
    status_barang = models.CharField(max_length=200,default='belum dibongkar',blank=True,null=True)
    jenis_sj_masuk = models.CharField(max_length=200,blank=True,null=True)#Pembelian/mutasi/retur jual
    modal_SJ_masuk = models.IntegerField(null=True,blank=True) #total nilai nota pembelian


class DetailSJMasuk(models.Model):
    id_detailSJM = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_masuk = models.CharField(max_length=200,blank=True,null=True)
    no_nota_masuk = models.CharField(max_length=200,blank=True,null=True)
    id_detail_nota_masuk = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_order = models.IntegerField(blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    asal_kiriman = models.CharField(max_length=200,blank=True,null=True) #asal perusahaan atau tempat barang ini dikirim
    jenis_sj_masuk = models.CharField(max_length=200,blank=True,null=True)
    harga_beli_pcs = models.IntegerField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)
    

class DetailLokasiMasukProduk(models.Model):
    no_nota_masuk = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_masuk = models.CharField(max_length=200,blank=True,null=True)
    kode_keluar_produk = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_produk = models.IntegerField(blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    harga_beli_pcs = models.IntegerField(null=True,blank=True)
    gudang_awal = models.CharField(max_length=200,blank=True,null=True)
    lokasi_produk = models.CharField(max_length=200,blank=True,null=True) # ada mekanisme buat detail lokasi gudang di tabel stok untuk menunjukan lokasi penyimpanan barang
    

class SJMasukRetur(models.Model):
    no_SJM_reutr = models.CharField(max_length=200,blank=True,null=True)
    no_nota_retur = models.CharField(max_length=200,blank=True,null=True)
    no_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    nama_pembawa = models.CharField(max_length=200,blank=True,null=True)
    waktu_masuk = models.DateTimeField(auto_now=False,blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    nama_penerima = models.CharField(max_length=200,blank=True,null=True)
    jenis_sj_masuk = models.CharField(max_length=200,blank=True,null=True)
    foto_notasj = models.ImageField(null=True,blank=True, upload_to="sjmasuk_img/")
    foto_bongkar = models.ImageField(null=True,blank=True, upload_to="sjmasuk_img/")
    status_confirmasi = models.BooleanField(blank=True,null=True)
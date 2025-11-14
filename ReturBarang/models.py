from django.db import models

# Create your models here.

class NotaRetur(models.Model):
    no_nota_retur = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_retur = models.CharField(max_length=200,blank=True,null=True)
    no_nota_jual = models.CharField(max_length=200,blank=True,null=True)
    tanggal_retur = models.DateField(auto_now=False,blank=True,null=True)
    nilai_nota_retur = models.CharField(max_length=200,blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)

class DetailRetur(models.Model):
    no_nota_retur = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_retur = models.CharField(max_length=200,blank=True,null=True)
    no_nota_jual = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_barang = models.IntegerField(null=True,blank=True)
    harga_jual = models.IntegerField(blank=True,null=True)
    harga_beli = models.IntegerField(blank=True,null=True)
    kondisi_barang = models.CharField(max_length=200,blank=True,null=True)
    id_detail_nota_jual = models.CharField(max_length=200,blank=True,null=True)

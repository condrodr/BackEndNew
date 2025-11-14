from django.db import models

# Create your models here.
class NotaPembelian(models.Model):
    no_nota_beli = models.CharField(max_length=200,blank=True,null=True)
    supplier = models.CharField(max_length=200,blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    faktur_atau_tidak = models.CharField(max_length=200,blank=True,null=True)
    hutang_standing = models.IntegerField(null=True,blank=True)
    diorder_oleh = models.CharField(max_length=200,blank=True,null=True)
    nilai_nota_beli = models.IntegerField(null=True,blank=True)
    tanggal_nota_beli = models.DateField(auto_now=False,blank=True,null=True)
    jatuh_tempo_beli = models.DateField(auto_now=False,blank=True,null=True)
    status_nota_beli = models.CharField(max_length=200,default='belum lunas',blank=True,null=True)
    status_barang_beli = models.CharField(max_length=200,default='belum dikirim',blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    total_volume_nota = models.CharField(max_length=200,blank=True,null=True)
    cluster_pembeli = models.CharField(max_length=200,blank=True,null=True,default='Cikebu')

class DetailPembelian(models.Model):
    no_nota_beli = models.CharField(max_length=200,blank=True,null=True)
    id_detail_nota_masuk = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_order_beli = models.IntegerField(blank=True,null=True)
    harga_beli_pcs = models.DecimalField(null=True,blank=True,max_digits=15,decimal_places=2)
    kantor_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    supplier = models.CharField(max_length=200,blank=True,null=True)
    tanggal_nota_beli = models.DateField(auto_now=False,blank=True,null=True)
    
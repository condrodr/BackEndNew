from django.db import models

# Create your models here.
class SJKeluar(models.Model):
    no_nota_keluar = models.CharField(max_length=200,blank=True,null=True) #bukan nota jual karena keluar barang belum tentu jualan
    no_SJ_keluar = models.CharField(max_length=200,blank=True,null=True) 
    no_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    nama_pengirim = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)
    gudang_awal = models.CharField(max_length=200,blank=True,null=True)
    tujuan_kirim = models.CharField(max_length=200,blank=True,null=True)
    jenis_sj_keluar = models.CharField(max_length=200,blank=True,null=True) #mutasi/penjualan/retur beli
    status_kiriman = models.CharField(max_length=200,blank=True,null=True, default='belum sampai')
    modal_SJ_keluar = models.IntegerField(blank=True,null=True) #menotalkan weighted average modal sebuah nota

class DetailSJKeluar(models.Model):
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_order = models.IntegerField(blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    no_nota_keluar = models.CharField(max_length=200,blank=True,null=True)
    id_detail_nota_keluar = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_keluar = models.CharField(max_length=200,blank=True,null=True)
    id_detailSJK = models.CharField(max_length=200,blank=True,null=True)
    tujuan_kirim = models.CharField(max_length=200,blank=True,null=True)
    jenis_sj_keluar = models.CharField(max_length=200,blank=True,null=True)
    harga_beli_produk = models.IntegerField(blank=True,null=True) #menjadi weighted lagi jika dari beberapa lokasi
    timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)

class DetailLokasiKeluarProduk(models.Model):
    no_nota_keluar = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_keluar = models.CharField(max_length=200,blank=True,null=True)
    kode_keluar_produk = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_produk = models.IntegerField(blank=True,null=True)
    harga_modal_produk = models.IntegerField(blank=True,null=True) #menjadi weighted average
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    gudang_awal = models.CharField(max_length=200,blank=True,null=True)
    lokasi_produk = models.CharField(max_length=200,blank=True,null=True) # ada mekanisme buat detail lokasi gudang di tabel stok untuk menunjukan lokasi penyimpanan barang
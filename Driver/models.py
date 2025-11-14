from django.db import models

# Create your models here.
class Driver(models.Model):
    no_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    nama_supir = models.CharField(max_length=200,blank=True,null=True)
    no_telepon_supir = models.CharField(max_length=200,blank=True,null=True)
    jenis_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    merek_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    tahun_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    status_kendaraan = models.CharField(max_length=200,blank=True,null=True,default="belum kerja")
    tarif_rupiah_per_km = models.IntegerField(null=True,blank=True)
    max_berat = models.IntegerField(null=True,blank=True)
    max_dus = models.IntegerField(null=True,blank=True)
    max_rupiah = models.IntegerField(null=True,blank=True)


class PlanKiriman(models.Model):
    no_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    id_plan_kiriman = models.CharField(max_length=200,blank=True, null=True)
    nomer_urut_kiriman = models.IntegerField(null=True,blank=True)
    nama_supir = models.CharField(max_length=200,blank=True, null=True)
    tanggal_kiriman = models.DateField(auto_now=False,blank=True, null=True) #Melambangkan kapan plan ini mau dikirim - untuk tanggal berapa
    total_jarak_km = models.IntegerField(null=True,blank=True)
    biaya_kiriman = models.IntegerField(null=True,blank=True)
    start_kerja = models.DateTimeField(auto_now=False,blank=True,null=True) # di aplikasi supir akan ada tombol start kerjaan
    selesai_kerja = models.DateTimeField(auto_now=False,blank=True,null=True) #Jika Supir Sudah kembali
    ada_returan = models.BooleanField(default=False) #Jika ada returan akan ada laporan masuk sini
    keterangan_retur = models.CharField(max_length=200,blank=True, null=True)

class DetailPlanKiriman(models.Model):
    no_nota_keluar = models.CharField(max_length=200,blank=True,null=True)
    no_sj_keluar = models.CharField(max_length=200,blank=True,null=True)
    jenis_transaksi = models.CharField(max_length=200,null=True,blank=True)
    nama_tujuan_kiriman = models.CharField(max_length=200,null=True,blank=True)
    GPS_lokasi_kiriman = models.CharField(max_length=200,null=True,blank=True)
    no_urut_kiriman = models.IntegerField(null=True,blank=True)
    id_plan_kiriman = models.CharField(max_length=200,null=True,blank=True)
    id_detail_plan_kiriman = models.CharField(max_length=200,blank=True,null=True)

class UpdateNotaKirimSebagian(models.Model):
    tujuan_kirim = models.CharField(max_length=200,null=True,blank=True)
    no_nota_keluar = models.CharField(max_length=200,null=True,blank=True) 
    nilai_belum_terkirim = models.CharField(max_length=200,null=True,blank=True) 
    terakhir_terkirim = models.CharField(max_length=200,null=True,blank=True)
    status_kiriman = models.CharField(max_length=200,null=200,blank=200)
    id_nota_sebagian = models.CharField(max_length=200,blank=True,null=True)

class DetailSisaNotaTerkirimSebagian(models.Model):
    no_nota_keluar = models.CharField(max_length=200,blank=True,null=True)
    id_detail_nota = models.CharField(max_length=200,blank=True,null=True)
    id_nota_sebagian = models.CharField(max_length=200,blank=True,null=True)
    tujuan_kirim = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_produk = models.IntegerField(blank=True,null=True)
    harga_jual_pcs = models.IntegerField(blank=True,null=True)
    discount_produk = models.FloatField(blank=True,null=True)
    subtotal_vol = models.FloatField(blank=True,null=True)
    jumlah_order_terkirim = models.IntegerField(blank=True,null=True)


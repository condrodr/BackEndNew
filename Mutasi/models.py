from django.db import models

# Create your models here

class NotaMutasiKeluarCart(models.Model):
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True,default='Pelumas') #Default tergantung app buat siapa
    gudang_awal = models.CharField(max_length=200,blank=True,null=True)
    tujuan_kirim = models.CharField(max_length=200,blank=True,null=True)
    nama_pengirim = models.CharField(max_length=200,blank=True,null=True)
    no_kendaraan = models.CharField(max_length=200,blank=True,null=True)
    tanggal_mutasi = models.DateField(blank=True,null=True,auto_now=False)
    no_mutasi = models.CharField(max_length=200,blank=True,null=True)
    jenis_mutasi = models.CharField(max_length=200,blank=True,null=True) #mutasi_normal/mutasi_perbaikan (mutasi perbaikan adalah untuk mutasi yang barang diterimanya kurang dari jumlah sebenarnya)
    status_kiriman = models.CharField(max_length=200,blank=True,null=True,default='belum dikirim') #belum dikirim/sedang dikirim/sudah dikirim
    nilai_mutasi = models.CharField(max_length=200,blank=True,null=True)
    keterangan_mutasi = models.CharField(max_length=200,blank=True,null=True,default='sesuai') #penyesuaian dibuat untuk no_mutasi (membenarkan mutasi yang salah)

class TerimaMutasiCart(models.Model):
    nama_penerima = models.CharField(max_length=200,blank=True,null=True)
    no_mutasi = models.CharField(max_length=200,blank=True,null=True)
    jenis_mutasi = models.CharField(max_length=200,blank=True,null=True) #mutasi normal atau penyesuaian
    tanggal_diterima = models.DateField(blank=True,null=True,auto_now=False)
    status_penerimaan = models.CharField(max_length=200,blank=True,null=True) #AdaBocor/Selisih/Sesuai/PenyesuaianSelesai
    keterangan_penerimaan = models.CharField(max_length=200,blank=True,null=True) #Detail bocor/selisih/sesuai

class DetailMutasiKeluarCart(models.Model):
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_order = models.IntegerField(blank=True,null=True)
    tanggal_mutasi = models.DateField(blank=True,null=True,auto_now=False)
    harga_modal_pcs = models.IntegerField(blank=True,null=True)
    no_mutasi = models.CharField(max_length=200,blank=True,null=True)
    id_detail_mutasi = models.CharField(max_length=200,blank=True,null=True)

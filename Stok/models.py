from django.db import models
from BackEndNew import choice as c

# Create your models here.
class StokUtama(models.Model):
    # Buat halaman untuk menginput real stok di gudang. Setelah submit nanti ada halaman yang hanya menampilkan produk yang hasil opname sengketa, jika diklik menampilkan kartu stoknya
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_barang = models.IntegerField(null=False, default=0)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    detail_lokasi = models.CharField(max_length=200,blank=True,null=True,default='Kosong',)
    harga_beli_weighted = models.IntegerField(null=False, default=0)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False,null=True,blank=True)

class KartuStok(models.Model):
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    tahun_produksi_produk = models.IntegerField(null=False, default=0)
    id_ks_transaksi = models.CharField(max_length=200,blank=True,null=True) #akan diambil dari id detail sjmasuk/keluar
    id_sj_transaksi = models.CharField(max_length=200,blank=True,null=True)
    jenis_transaksi = models.CharField(max_length=200,blank=True,null=True)
    detail_lokasi = models.CharField(max_length=200,blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    jumlah_transaksi = models.IntegerField(null=False, default=0)
    estimasi_harga_beli = models.IntegerField(null=False, default=0)
    stok_awal = models.IntegerField(null=False,default=0)
    stok_akhir = models.IntegerField(null=False,default=0)
    timestamp = models.DateTimeField(auto_now=False,null=True,blank=True)
    keterangan = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)


class StokTransit(models.Model):
    #Ini adalah stok extra diluar SJ Masuk - SJ Keluar karena barang masih on transit
    no_nota_transit = models.CharField(max_length=200,blank=True,null=True)
    no_SJ_keluar = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False,null=True,blank=True)
    harga_modal_pcs = models.IntegerField(null=True,blank=True)
    jumlah_barang = models.IntegerField(null=False, default=0)
    tujuan_kirim = models.CharField(max_length=200,blank=True,null=True)
    jenis_transit = models.CharField(max_length=200,blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)

class SelisihBongkarMuat(models.Model):
    id_sj_transaksi = models.CharField(max_length=200,blank=True,null=True)
    id_ks_transaksi = models.CharField(max_length=200,blank=True,null=True)
    jenis_transaksi = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    jumlah_selisih = models.IntegerField(null=False, default=0)
    timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)
    keterangan = models.CharField(max_length=200,blank=True,null=True) #Penyebab Selisih atau informasi tentang selisih
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    status_selisih = models.CharField(max_length=200,blank=True,null=True)#belum terselesaikan/terselesaikan

class AuditStok(models.Model):
    id_audit_stok = models.CharField(max_length=200,blank=True,null=True)
    nama_produk = models.CharField(max_length=200,blank=True,null=True)
    kode_produk = models.CharField(max_length=200,blank=True,null=True)
    detail_lokasi = models.CharField(max_length=200,blank=True,null=True)
    stok_fisik_teraudit = models.IntegerField(null=False, default=0)
    stok_utama_buku = models.IntegerField(null=False, default=0)
    selisih = models.IntegerField(null=False, default=0)
    keterangan = models.CharField(max_length=200, blank=True,null=True)
    gudang_cabang = models.CharField(max_length=200, blank=True,null=True)
    jumlah_barang = models.IntegerField(null=False, default=0)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)
    user_id = models.CharField(max_length=200,blank=True,null=True)



class LokasiStok(models.Model):
    nama_lokasi = models.CharField(max_length=200,blank=True,null=True) #Buatkan nama lokasi seperti A1, A2 dsb
    deskripsi_lokasi = models.CharField(max_length=200,blank=True,null=True) #ini adalah verbal penjelasan dimana lokasinya, misal atas kanan
    foto_lokasi = models.ImageField(null=True,blank=True,upload_to='photo_lokasi_gudang/')
    gudang_cabang = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    jenis_lokasi =  models.CharField(max_length=200,blank=True,null=True,default='Kosong',choices=c.choice_jenis_lokasi)
    #AIAutoCount Ada dashbord yg menampilkan sudah aicount, tombol snapshot cek hasil snapshoot. api, 
    #Volume Lokasi 20 Mei tambahkan dimensi lokasi
    #Estimasi space misal 200 dalam dus 20 x 1 besar

    
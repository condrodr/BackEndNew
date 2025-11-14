from django.db import models
from BackEndNew import choice as c

class Produk(models.Model):
    #General Informasi Terkait Produk
    nama_produk = models.CharField(max_length=200,blank=True,null=True) #nama lengkap produk
    alias_produk = models.CharField(max_length=200,blank=True,null=True) #nama singkat produk
    kode_produk = models.CharField(max_length=200,blank=True,null=True) #ini yang akan kita pakai untuk pivot data
    kimap_produk = models.CharField(max_length=200,blank=True,null=True) #ini yang akan jadi jembatan produk kita dengan prinsipal
    photo_produk_1 = models.ImageField(null=True,blank=True,default="blackdwarf.jpg",upload_to="produk_img_1/") #ini adalah foto utama produk tampak depan
    photo_produk_2 = models.ImageField(null=True,blank=True,default="blackdwarf.jpg",upload_to="produk_img_2/") #ini adalah foto kedua produk tampak belakang
    photo_produk_3 = models.ImageField(null=True,blank=True,default="blackdwarf.jpg",upload_to="produk_img_3/") #ini adalah foto ketiga produk tampak lain
    photo_produk_4 = models.ImageField(null=True,blank=True,default="blackdwarf.jpg",upload_to="produk_img_4/") #ini adalah foto keempat produk tampak lain
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_kemasan) #ini adalah jenis kemasan produk seperti dus atau drum
    isi_per_pack = models.IntegerField(null=True,blank=True,choices=c.choice_isi_pack) #ini adalah jumlah isi produk dalam 1 pack    #1Palet ada berapa pack/dus Tambah dus_per_palet
    dus_per_palet = models.IntegerField(null=True,blank=True)
    volume_per_pcs = models.FloatField(null=True,blank=True,choices=c.choice_volume_pcs) #ini adalah volume produk per pcs atau berat per pack untuk non liquid
    #AI generated
    deskripsi_produk = models.TextField(max_length=400,blank=True,null=True) #ini adalah deskripsi produk yang bisa digenerate dengan AI untuk SEO
    fungsi_produk = models.CharField(max_length=200,blank=True,null=True) #ini adalah penjelasan pengguna produk seperti untuk motor matic, oli samping, dsb bisa dibuatkan oleh AI
    #Terkait Informasi Harga Produk (Semua Include PPN)
    harga_HET_pcs = models.IntegerField(null=True,blank=True) #ini adalah harga rekomendasi jual ke end user
    harga_HTO_pcs = models.IntegerField(null=True,blank=True) #ini adalah harga jual ke outlet atau setara JPC lama dengan standar margin 8% dari harga beli
    harga_beli_per_pack = models.IntegerField(null=True,blank=True) #ini adalah harga tebus produk setelah ppn, angka asli yang kita keluarkan buat beli
    #Kategorization dari Produk Untuk Multi Filter
    merek_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_merek) #ini adalah merek produk seperti MPX/Enduro/Mesran/Meditran/Helix/Advance/Federal/Mobil
    submerek_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_submerek) #ini adalah submerek produk seperti Enduro Racing, Enduro Matic S
    tiersegmen_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_tier) #ini adalah tier produk untuk mahal atau highend atau untuk murah atau lowend HT/NHT
    usersegmen_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_user) #ini adalah segmentasi pengguna bisa 2W/4W/6W/Mesin Industrial
    kategori_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_kategori) #ini adalah kategori produk seperti Ban, Oli, Aki, Busi Sparepart
    klasifikasi_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_klasifikasi) #ini adalah klasifikasi produk untuk Retail (dijual di toko toko) atau untuk industry (dijual langsung ke pabrik/end user)
    spek_produk = models.CharField(max_length=200,blank=True,null=True) #ini adalah spek teknis produk seperti sae/size ban/spek lain
    produsen_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_produsen) #ini adalah perusahaan utama produsen merek ini seperti Pertamina/Exxon/Shell/AHM
    jenis_produk = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_jenis) #ini adalah penggolongan produk ke fast_moving/slow_moving
    #Kepentingan Internal Applikasi
    timestamp = models.DateTimeField(auto_now=True) #ini adalah waktu data ini dibuat atau diupdate
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_divisi_kantor) #ini adalah divisi kantor mana yang menggunakan applikasi ini
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_perusahaan_kantor) #ini adalah nama PT yang menggunakan applikasi ini, pertamina dengan gelora dan non pertamina dengan portalindo atau lain
    # tambahan Dimensi produk. 20 Mei

#Ini digunakan untuk Promosi Internal di Perusahaan (Jenis Promosi yang bisa dilakukan dengan ini adalah FlashSale sell in Spesifik Produk)
#Ini jenis promo simple yang kita state produk A dipromo kan dan berlaku untuk semua outlet
class ProdukPromotion(models.Model):
    nama_promo = models.CharField(max_length=200,blank=True,null=True) #ini adalah nama promo kita
    tipe_promo = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_tipe_promo) #ini adalah segmen promo (single produk,by merek,by submerek,by tiersegmen,by usersegmen,by kategori,by klasifikasi,by spek,by produsen,by jenis,all produk)
    yang_dipromokan = models.CharField(max_length=200,blank=True,null=True) #ini adalah yang dipromokan, jika single produk maka choice = kode_produk, jika kategorial maka choice = tergantung kategorinya (cek kategorization diatas)
    status_promo = models.BooleanField(default=False) #ini adalah status apakah promo masih aktif atau sudah selesai
    deskripsi_promo = models.CharField(max_length=200,blank=True,null=True) #ini adalah teknis penjelasan promo
    diskon_promo = models.CharField(max_length=200,blank=True,null=True) #ini adalah harga maximal promo/max diskon untuk jenis flashsale atau cost ratio reward untuk jenis kontrak
    dimulai_tanggal = models.DateField(auto_now=False,blank=True,null=True) #ini adalah periode promo dimulai
    berakhir_tanggal= models.DateField(auto_now=False,blank=True,null=True) #ini adalah periode promo berakhir

 
    

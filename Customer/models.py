from django.db import models
from BackEndNew import choice as c

class RegisteredCustomer(models.Model):
####Data General Informasi Tentang Konsumen:######
    nama_outlet = models.CharField(max_length=200,blank=True,null=True) #nama perusahaan atau customer
    nama_pemilik = models.CharField(max_length=200,blank=True,null=True) #ini adalah keterangan nama pemilik outlet
    no_telepon_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah nomer telepon outlet, pastikan ini nomer utama yang ada wa nya
    no_telepon_lain_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah nomer kedua outlet
    kode_outlet = models.CharField(max_length=200,blank=True,null=True) #kode yang akan kita pakai buat pivot data dan calling di dalam internal code kita
    kode_prinsipal_outlet = models.CharField(max_length=200,blank=True,null=True) #kode DMS adalah unik kode buat jembatan database kita dan pemilik merek, jika belum ada, seharusnya statusnya belum ada
    photo_tampak_depan = models.ImageField(null=True,blank=True,upload_to='photo_tampak_depan/') #ini adalah foto tampak depan outlet
    photo_display_outlet = models.ImageField(null=True,blank=True,upload_to='photo_display_outlet/') #ini adalah foto display produk di outlet
    photo_kondisi_outlet = models.ImageField(null=True,blank=True,upload_to='photo_kondisi_outlet/') #ini adalah foto kondisi outlet baik bengkelnya ataupun jumlah karyawannya
    deskripsi_outlet = models.CharField(max_length=200,blank=True,null=True) #ini akan menjadi AI generated content berdasarkan semua data yang diupdate 1 tahun sekali secara otomatis dengan timer
    no_KTP_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah nomer ktp pemilik outlet
    photo_ktp_pemilik = models.ImageField(null=True,blank=True,upload_to='photo_ktp_pemilik/') #ini adalah foto ktp pemilik outlet
    no_NPWP_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah nomer NPWP jika outlet sudah memiliki NPWP dan kemungkinan butuh faktur
    jumlah_pekerja = models.IntegerField(null=True,blank=True) #ini adalah data jumlah karyawan di outlet, pastikan yang sedang tidak shift pun dihitung
    GPS_lokasi_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah lokasi GPS google map dari outlet harus tepat persis di depan outlet sekali klik map
    Google_Place_ID = models.CharField(max_length=200,blank=True,null=True) #ini adalah kode Place ID untuk synkron data Google dengan data kita
    alamat_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah alamat tertulis dari outlet sesuai google map
    kelurahan_outlet = models.CharField(max_length=400,blank=True,null=True) #ini adalah alamat kelurahan outlet
    kecamatan_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah alamat kecamatan outlet
    kabupaten_outlet = models.CharField(max_length=400,blank=True,null=True) #ini adalah alamat kabupaten outlet
    provinsi_outlet = models.CharField(max_length=400,blank=True,null=True) #ini adalah alamat provinsi outlet
    kategori_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_kategori_outlet) #menentukan jenis konsumen 2W,4W,6W,2W4W,4W6W,2W6W,2W4W6W,pabrik,tambang,alat berat,subcon,crusher,kapal tangker,kapal nelayan,pembangkit,PO Bus,trucking,transportir,perkebunan,peternakan,pengolahan
    level_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_level_outlet) #ini adalah level konsumen kecil,besar,sedang atau sangat besar
    tipe_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_tipe_outlet)
    # pic_dms = models.CharField(max_length=200,blank=True,null=True)
    # rute_dms = models.CharField(max_length=200,blank=True,null=True)
    # frekuensi_dms = models.CharField(max_length=200,blank=True,null=True)
        #ini adalah tipe bisnis outlet Kelilingan, Toko, Bengkel, SPBU, Industry, KAM, ATPM, Bengkel Own Channel
        #Kelilingan, Toko, Bengkel, SPBU, ATPM, Bengkel Own Channel = Outlet Retail, Industry = Outlet Industry, KAM = Outlet KAM
    bentuk_usaha_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_bentuk_usaha_outlet)
        #ini adalah bentuk usaha outlet: PT, CV, Koperasi, Yayasan, UD, BUMN, BUMD, Perorangan
####Data Spesifik Bisnis di Outlet:#####    
    #ini adalah data untuk icon outlet mempercepat melakukan pengecekan apa yang dijual outlet:
    sedia_oli_dus_tidak = models.BooleanField(default=False)
    sedia_drum_tidak = models.BooleanField(default=False)
    sedia_ban_tidak = models.BooleanField(default=False)
    sedia_aki_tidak = models.BooleanField(default=False)
    sedia_sparepart_tidak = models.BooleanField(default=False)
    bisnis_fokus_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_bisnis_fokus_outlet) #untuk tahu apa produk paling dominan, icon produk yang dominan kita ganti warna
    apa_oli_paling_dominan_disini = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_oli_dominan) #untuk tahu apa produk oli yang paling laku di daerah ini
        #mana yang paling laku ban,oli,aki,sparepart,drum di tempat ini
    supplier_di_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah data biasanya outlet ini beli dari siapa saja 
    merek_tersedia_di_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah merek apa saja yang dilihat ada di outlet ini
    jumlah_pelanggan_sehari = models.IntegerField(null=True,blank=True) #ini adalah jumlah pelanggan masuk sehari untuk menghitung potensi omset
    lebar_muka_jalan = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_lebar_muka_jalan) #ini adalah estimasi lebar depan outlet: lebih kecil dari 4m, 4-8m, 8m ++
    tipe_lokasi_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_tipe_lokasi_outlet) #ini adalah status jalan letak outlet, apakah: R1(jalan bisa 2 mobil papasan tidak sempit), R2(jalan sempit buat 2 mobil lewat papasan), R3(jalan hanya bisa 1 mobil masuk), R4(jalan tidak bisa dilewati mobil)
    estimasi_nilai_stok = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_estimasi_nilai_stok) #ini adalah estimasi nilai stok di outlet apakah: dibawah 5 juta, 5-20 juta atau diatas 20 juta
    discount_level_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah level diskon di outlet -1,-2,-3,-4,-5,-6,-7 dari JPC
    photo_form_fasilitas_kredit = models.ImageField(null=True,blank=True,upload_to='photo_form_fasilitas_kredit/') #ini adalah foto form fasilitas kredit pemilik outlet khusus untuk konsumen yang mau beli tempo
    photo_form_pdp = models.ImageField(null=True,blank=True,upload_to='photo_form_pdp/') #ini adalah foto form persetujuan penggunaan data dan perlindungan data konsumen
    apa_tempat_milik_sendiri = models.BooleanField(default=False) #mengukur resiko bisnis, apakah tempat ini milik sendiri / sewa
    plafon_outlet = models.IntegerField(null=True,blank=True) #ini adalah level plafon yang diberikan manager kepada outlet
    target_jual = models.IntegerField(null=True,blank=True) #ini adalah angka target penjualan di outlet yang diisi oleh manager
    top100 = models.BooleanField(default=False) #ini adalah status apakah outlet masuk ke top konsumen kita
    jenis_bayar = models.CharField(max_length=200,blank=True,null=True) #ini adalah jenis pembayaran outlet: cash, tempo atau cicil
    tipe_bayar = models.CharField(max_length=200,blank=True,null=True) #ini adalah tipe bayar outlet: Transfer, Tunai, BG, Jasa
    status_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah status di outlet: Normal, Waspada, BlackList. BlackList berarti wajib cash
    hari_kebiasaan_belanja = models.CharField(max_length=200,blank=True,null=True) #ini adalah informasi biasanya outlet belanja di hari apa? Kita wajib wa penawaran 1 hari sebelumnya
    audio_interview_outlet = models.FileField(upload_to='audio/',null=True,blank=True) #ini adalah data rekaman interview di outlet
    
####Data Internal Perusahaan Ke Outlet:#####
    cluster_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_cluster_outlet) #ini adalah cluster tempat kita kerja
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_divisi_kantor) #ini adalah divisi tempat kita kerja dan outlet ini dibawah divisi apa
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_perusahaan_kantor) #ini adalah nama PT yang menggunakan applikasi ini, pertamina dengan gelora dan non pertamina dengan portalindo atau lain
    nama_salesman = models.CharField(max_length=200,blank=True,null=True) #ini adalah nama salesman yang menghandle outlet ini
    rute_kunjungan = models.CharField(max_length=200,blank=True,null=True,default='belum ada',choices=c.choice_rute_kunjungan) #ini adalah jadwal rute kunjungan sales yang menghandle outlet ini
    frequency_kunjungan = models.CharField(max_length=200,blank=True,null=True,default='belum ada',choices=c.choice_rute_kunjungan) #ini adalah f1, f2 kunjungan sales yang menghandle outlet ini
    timestamp = models.DateTimeField(auto_now=True) #ini adalah data waktu kapan data ini terakhir di update
    catatan_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah catatan di outlet oleh manager terkait konsumen ini
    loyalty_level = models.IntegerField(null=True,blank=True) #ini adalah level loyalitas outlet kepada kita, dinilai dari 6 bulan terakhir transaksi 1 hati setiap tidak bolong


class LoyaltyPointCustomer(models.Model):
    kode_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah kode outlet buat pivot data pemilik point
    tipe_transaksi = models.CharField(max_length=200,blank=True,null=True) #ini adalah tipe transaksi loyalty, redeem berarti 'keluar', dapat point berarti 'masuk'
    loyalty_point = models.IntegerField(null=True,blank=True) #ini adalah jumlah loyalty point dalam transaksi baik keluar maupun masuk 5perak dari setiap transaksi
    timestamp = models.DateTimeField(auto_now=True) #ini adalah timestamp dari transaksi di outlet
    loyalty_transaction_id = models.CharField(max_length=200,blank=True,null=True) #ini adalah unik code buat mencatat setiap transaksi loyalty point
    loyalty_heart = models.CharField(max_length=200,blank=True,null=True) #ini 


class DataPotensiCustomer(models.Model):
####Ini adalah data Leads dari Potensi Customer di area kita####
    nama_outlet = models.CharField(max_length=200,blank=True,null=True) #nama perusahaan atau customer
    kode_potensi_customer = models.CharField(max_length=200,blank=True,null=True) #ini adalah unik kode potensi customer untuk internal kita
    kode_prinsipal_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah unik kode untuk menyamakan data potensi customer kita dengan prinsipal
    GPS_lokasi_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah lokasi GPS google map dari outlet harus tepat persis di depan outlet sekali klik map
    Google_Place_ID = models.CharField(max_length=200,blank=True,null=True) #ini adalah unik kode untuk menyamakan data kita dengan google
    nama_pemilik = models.CharField(max_length=200,blank=True,null=True) #ini adalah keterangan nama pemilik outlet
    no_telepon_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah nomer telepon outlet, pastikan ini nomer utama yang ada wa nya 
    kategori_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_kategori_outlet) #menentukan jenis konsumen 2W,4W,6W,2W4W,4W6W,2W6W,2W4W6W,pabrik,tambang,alat berat,subcon,crusher,kapal tangker,kapal nelayan,pembangkit,PO Bus,trucking,transportir,perkebunan,peternakan,pengolahan
    level_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_level_outlet) #ini adalah level konsumen kecil,besar,sedang atau sangat besar
    tipe_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_tipe_outlet)
        #ini adalah tipe bisnis outlet Kelilingan, Toko, Bengkel, SPBU, Industry, KAM, ATPM, Bengkel Own Channel
        #Kelilingan, Toko, Bengkel, SPBU, ATPM, Bengkel Own Channel = Outlet Retail, Industry = Outlet Industry, KAM = Outlet KAM
    bentuk_usaha_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_bentuk_usaha_outlet)
        #ini adalah bentuk usaha outlet: PT, CV, Koperasi, Yayasan, UD, BUMN, BUMD, Perorangan
####Data Spesifik Bisnis di Outlet:#####    
    #ini adalah data untuk icon outlet mempercepat melakukan pengecekan apa yang dijual outlet:
    sedia_oli_dus_tidak = models.BooleanField(default=False)
    sedia_drum_tidak = models.BooleanField(default=False)
    sedia_ban_tidak = models.BooleanField(default=False)
    sedia_aki_tidak = models.BooleanField(default=False)
    sedia_sparepart_tidak = models.BooleanField(default=False)
    bisnis_fokus_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_bisnis_fokus_outlet) #mana yang paling laku ban,oli,aki,sparepart,drum di tempat ini
    supplier_di_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah data biasanya outlet ini beli dari siapa saja
    merek_tersedia_di_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah merek apa saja yang dilihat ada di outlet ini
    jumlah_pekerja = models.IntegerField(null=True,blank=True) #ini adalah data jumlah karyawan di outlet, pastikan yang sedang tidak shift pun dihitung
    jumlah_pelanggan_sehari = models.IntegerField(null=True,blank=True) #ini adalah data jumlah pelanggan masuk sehari untuk menghitung potensi outlet
    lebar_muka_jalan = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_lebar_muka_jalan) #ini adalah estimasi lebar depan outlet: lebih kecil dari 4m, 4-6m, 6-8m, 8-12m, 12m ++
    tipe_lokasi_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_tipe_lokasi_outlet) #ini adalah status jalan letak outlet, apakah: R1(jalan bisa 2 mobil papasan tidak sempit), R2(jalan sempit buat 2 mobil lewat papasan), R3(jalan hanya bisa 1 mobil masuk), R4(jalan tidak bisa dilewati mobil)
    estimasi_nilai_stok = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_estimasi_nilai_stok) #ini adalah estimasi nilai stok di outlet apakah: dibawah 5 juta, 5-20 juta atau diatas 20 juta
    kondisi_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_kondisi_outlet)
        #terawat = spanduk relatif baru, outlet dan stok terpajang bersih
        #kurang terawat = bangunan dan stok kotor, butuh pengecatan dan perbaikan ringan
        #tidak terawat = stok minim, kotor, bahkan peralatan pun minim, buka tutup tidak normal
    urgency_outlet = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_urgency)
        #nilai 0 = tidak potensi (baik karena pernah macet ataupun lain sebagainya)
        #nilai 1 = jika outlet ini berpotensi
        #nilai 2 = jika outlet sudah masuk rute
        #nilai 3 = jika outlet ini potensi tapi bukan pemain oli (toko ban dan aki)
        #nilai 4 = jika ini outlet dari sales hunter pertamina ada dms tapi tidak ada di kita

class DailyRegisteredCustomerReport(models.Model):
####Ini adalah Data yang Time Series dan bergerak dari Outlet ####
    kode_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah kode outlet buat pivot data pemilik outlet
    timestamp = models.DateTimeField(auto_now=True) #ini adalah timestamp dari terakhir data daily terbaru diupdate
    update_kondisi_outlet = models.CharField(max_length=200,blank=True,null=True) #ini didapat dari pertanyaan bagaimana kondisi minggu ini, sepi atau ramai?
    update_merek_kompetitor = models.CharField(max_length=200,blank=True,null=True) #ini didapat dari pertanyaan belakangan ini merek paling laku merek apa?
    alasan_belum_order = models.CharField(max_length=200,blank=True,null=True) #ini adalah kewajiban sales menjawab kenapa outlet yang dikunjungin belum order
    update_pesaing = models.CharField(max_length=200,blank=True,null=True) #jika kalah harga atau tempo infokan siapa yang nawarin dan harga berapa
    update_keterangan = models.CharField(max_length=200,blank=True,null=True) #infokan jika ada berita lain seperti promo pesaing atau pemilik sakit atau apapun itu
    estimasi_jumlah_stok_terlihat = models.CharField(max_length=200,blank=True,null=True) #ini menunjukan estimasi rupiah nilai stok di outlet (sales kita harus dilatih untuk ini), dibawah 5 juta, 5-10 juta, 10-20 juta, 20-30 juta, 30 juta ++
    update_kondisi_outlet = models.CharField(max_length=200,blank=True,null=True) #ceritakan apapun itu terkait kondisi outlet seperti: habis renovasi atau rebranding apapun itu, makin kurang terawat mungkin owner menua mulai sakit, mulai terlihat parah bahkan stok dan karyawan habis

#Ini digunakan untuk Promosi berjenis Kontrak Konsumen memberikan spesifik target segmen tertentu di konsumen
#Ini jenis promo kompleks customized per customer dengan memberi mereka target kontrak
class KontrakOutletPromotion(models.Model):
    nama_promo = models.CharField(max_length=200,blank=True,null=True) #ini adalah nama kontrak promo yang dibuat
    kode_outlet = models.CharField(max_length=200,blank=True,null=True) #ini adalah kode outlet yang ikut kontrak ini
    data_keikutsertaan = models.ImageField(null=True,blank=True,upload_to='kontrak_outlet/data_keikutsertaan')
    status_promo = models.BooleanField(default=False) #ini adalah status apakah promo masih aktif atau sudah selesai
    target_promo = models.CharField(max_length=200,blank=True,null=True) #ini adalah target promo dalam liter/rupiah tergantung ketentuan
    dimulai_tanggal = models.DateField(auto_now=False,blank=True,null=True) #ini adalah periode promo dimulai
    berakhir_tanggal= models.DateField(auto_now=False,blank=True,null=True) #ini adalah periode promo berakhir

class DaftarPromosiBerjalan(models.Model):
    nama_promo = models.CharField(max_length=200,blank=True,null=True) #ini adalah nama kontrak promo yang dibuat
    tipe_promo = models.CharField(max_length=200,blank=True,null=True,) #ini adalah jenis promo single produk atau kategorial (single produk,by merek,by submerek,by tiersegmen,by usersegmen,by kategori,by klasifikasi,by spek,by produsen,by jenis,all produk)
    pembuat_promo = models.CharField(max_length=200,blank=True,null=True,)
    deskripsi_promo = models.CharField(max_length=200,blank=True,null=True) #ini adalah teknis penjelasan promo
    yang_dipromokan = models.CharField(max_length=200,blank=True,null=True) #ini adalah yang dipromokan, jika single produk maka choice = kode_produk, jika kategorial maka choice = tergantung kategorinya (cek kategorization di Produk.Model)
    wajib_upload_tidak = models.BooleanField(default=False)
    alias_promo = models.CharField(max_length=10,blank=True,null=True) # miring italic fontnya ukuran 8


class Prompt(models.Model):
    prompt_id = models.CharField(max_length=200,null=True,blank=True)
    prompt_name = models.CharField(max_length=200,null=True,blank=True)
    default_prompt = models.TextField(null=True, blank=True)
    adjusted_prompt = models.TextField(null=True, blank=True)
    prompt_description =  models.CharField(max_length=200,null=True,blank=True)
    lokasi_prompt = models.CharField(max_length=200,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=False,blank=True,null=True)
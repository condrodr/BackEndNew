from django.db import models

# Create your models here.
class Profile(models.Model):
    #User profile
    username = models.CharField(max_length=200,blank=True,null=True)
    password = models.CharField(max_length=200,blank=True,null=True)
    kategori_akun = models.CharField(max_length=200,blank=True,null=True) # sales, admin, spv, manager, external, pemilik toko
    jabatan_user = models.CharField(max_length=200,blank=True,null=True) # Sales_Cilacap_Barat, Supervisor_Cikebu, nama_toko
    authorisasi = models.CharField(max_length=200,blank=True,null=True) # authorisasi level 1, level 2, level 3
    profil_kode = models.CharField(max_length=200,blank=True,null=True)
    user_id = models.IntegerField(blank=True,null=True)

    #KYC Data
    nama_lengkap = models.CharField(max_length=200,blank=True,null=True)
    tanggal_lahir = models.DateField(auto_now=False)
    no_KTP = models.CharField(max_length=200,blank=True,null=True)
    alamat_KTP = models.CharField(max_length=200,blank=True,null=True)
    phone_number = models.CharField(max_length=200,blank=True,null=True)

    #Terkait Internal
    cluster = models.CharField(max_length=200,blank=True,null=True)
    perusahaan_kantor = models.CharField(max_length=200,blank=True,null=True)
    divisi_kantor = models.CharField(max_length=200,blank=True,null=True)
    kantor_cabang = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=True)

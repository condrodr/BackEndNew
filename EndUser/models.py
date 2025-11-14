from django.db import models


class Rekomender(models.Model):
    id_rekomender = models.CharField(max_length=200,blank=True,null=True)
    nama_rekomender = models.CharField(max_length=200,blank=True,null=True)
    dms_rekomender = models.CharField(max_length=200,blank=True,null=True)
    kode_outlet = models.CharField(max_length=200,blank=True,null=True)
    no_telp = models.CharField(max_length=200,blank=True,null=True)
    foto_qr = models.ImageField(upload_to="uploads/qrcode/", blank=True, null=True)
    budget_per_liter = models.IntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return f"{self.nama_rekomender} ({self.kode_outlet})"


class RewardSpinWheel(models.Model):
    id_reward =models.CharField(max_length=200,blank=True,null=True)
    kode_dms = models.CharField(max_length=200,blank=True,null=True)
    nama_reward = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return f"{self.nama_reward} - {self.kode_dms}"

class RewardList(models.Model):
    nama_outlet = models.CharField(max_length=200,blank=True,null=True)
    probabilitas = models.CharField(max_length=200,blank=True,null=True)
    kode_dms = models.CharField(max_length=200,blank=True,null=True)
    nama_barang = models.CharField(max_length=200,blank=True,null=True)
    jumlah_barang = models.IntegerField(null=True,blank=True,default=0)


class JualanRekomender(models.Model):
    id_rekomender = models.CharField(max_length=200,blank=True,null=True)
    rekomender = models.CharField(max_length=200,blank=True,null=True)
    dms_rekomender = models.CharField(max_length=200,blank=True,null=True)
    produk_dijual = models.CharField(max_length=200,blank=True,null=True)
    jumlah_produk = models.IntegerField(blank=True,null=True)
    kemasan_produk = models.CharField(max_length=200,blank=True,null=True)
    nama_pembeli = models.CharField(max_length=200,blank=True,null=True)
    no_telp_pembeli = models.CharField(max_length=200,blank=True,null=True)
    foto_upload = models.ImageField(upload_to="uploads/rekomender/", blank=True, null=True)
    reward_spin_wheel = models.CharField(max_length=200,blank=True,null=True)
    reward_rekomender = models.CharField(max_length=200,blank=True,null=True)
    tanggal = models.DateField(auto_now=True)
    status_reward_rekomender = models.CharField(
        max_length=50,
        choices=[
            ("Belum diberikan", "Belum diberikan"),
            ("Sudah diberikan", "Sudah diberikan")
            
        ],
        default="Belum diberikan"
    )

    def __str__(self):
        return f"{self.produk_dijual} oleh {self.nama_pembeli}"

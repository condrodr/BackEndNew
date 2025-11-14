from django.db import models
from BackEndNew import choice as c
# Create your models here.

class AkunPembukuan(models.Model):
    nama_akun = models.CharField(max_length=200,blank=True,null=True)
    kode_akun = models.CharField(max_length=200,blank=True,null=True)
    tipe_akun = models.CharField(max_length=200,blank=True,null=True,choices=c.choice_tipe_akun)
    deskripsi_akun =  models.CharField(max_length=200,blank=True,null=True)


# class JournalEntry(models.Model):
#    # deskripsi = models.CharField(max_length=200,blank=True,null=True)
#     kategori_action = models.CharField(max_length=200,blank=True,null=True)
#     detaildeskripsi = models.CharField(max_length=200,blank=True,null=True)
#     timestamp = models.DateField(auto_now=True,blank=True,null=True)
#     kode_entry =  models.CharField(max_length=200,blank=True,null=True)
#     validitas =  models.CharField(max_length=200,blank=True,null=True)


# class JournalEntryLine(models.Model):
#     kode_entry =  models.CharField(max_length=200,blank=True,null=True)
#     nama_akun =  models.CharField(max_length=200,blank=True,null=True)
#     kode_akun =  models.CharField(max_length=200,blank=True,null=True)
#     date = models.DateField(auto_now=False,blank=True,null=True)
#     tipe_journal = models.CharField(max_length=200,blank=True,null=True)
#     value_transaksi = models.CharField(max_length=200,blank=True,null=True)



from django.db import models

# Create your models here.
class Salesman(models.Model):
    nama_sales = models.CharField(max_length=200,blank=True,null=True)
    kas_disales = models.IntegerField(null=True,blank=True)
    target_minimum = models.IntegerField(blank=True,null=True)
    target_incentive = models.IntegerField(null=True,blank=True)


class CatatanSalesman(models.Model):
    nama_sales = models.CharField(max_length=200,blank=True,null=True)
    tugas_ke_sales = models.CharField(max_length=200,blank=True,null=True)#saat briefing spv bisa memberi tugas ke sales c
    catatan_ke_sales = models.CharField(max_length=200,blank=True,null=True)
    info_dari_sales = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateField(auto_now=False,null=True,blank=True)


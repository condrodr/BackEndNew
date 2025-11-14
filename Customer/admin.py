from django.contrib import admin
from Customer.models import RegisteredCustomer
# Register your models here.

class RegisteredCustomerAdmin(admin.ModelAdmin):
    list_display = [
            'nama_outlet',


            'kode_outlet',
            'kabupaten_outlet',

            'nama_salesman',
            'cluster_outlet',
            'rute_kunjungan',
           
            
            
    ]
    
    search_fields = ('nama_outlet','kode_outlet')

admin.site.register(RegisteredCustomer, RegisteredCustomerAdmin)
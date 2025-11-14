from django.contrib import admin
from .models import JualanRekomender, Rekomender, RewardList, RewardSpinWheel
# Register your models here.
class JualanRekomenderAdmin(admin.ModelAdmin):
    list_display = [
            'id_rekomender',
            'produk_dijual',
            'jumlah_produk'
           
    ]
    
    search_fields = ('produk_dijual','rekomender')

admin.site.register(JualanRekomender, JualanRekomenderAdmin)

class RekomenderAdmin(admin.ModelAdmin):
    list_display = [
            'id_rekomender',
            'nama_rekomender',
            'dms_rekomender'
           
    ]
    

admin.site.register(Rekomender, RekomenderAdmin)

class RewardListAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'nama_outlet',
            'probabilitas',
            'kode_dms',
            'nama_barang'
           
    ]
    

admin.site.register(RewardList, RewardListAdmin)

class RewardSpinWheelAdmin(admin.ModelAdmin):
    list_display = [
            'id_reward',
            'kode_dms',
            'nama_reward',
    ]
    

admin.site.register(RewardSpinWheel, RewardSpinWheelAdmin)
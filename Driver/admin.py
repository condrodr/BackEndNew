from django.contrib import admin
from .models import Driver,  PlanKiriman, DetailPlanKiriman, UpdateNotaKirimSebagian, DetailSisaNotaTerkirimSebagian
# Register your models here.

admin.site.register(Driver)
admin.site.register(PlanKiriman)
admin.site.register(DetailPlanKiriman)
admin.site.register(UpdateNotaKirimSebagian)
admin.site.register(DetailSisaNotaTerkirimSebagian)
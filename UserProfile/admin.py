from django.contrib import admin
from UserProfile.models import Profile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
            'username',
            'password',
            'kategori_akun',
            'jabatan_user',
            'authorisasi',
            'profil_kode',
            'nama_lengkap',
            'tanggal_lahir',
            'no_KTP',
            'alamat_KTP',
            'phone_number',
            'cluster',
            'perusahaan_kantor',
            'divisi_kantor',
            'kantor_cabang',
            'timestamp',

    ]
    
    search_fields = ('username','jabatan_user')


admin.site.register(Profile,UserProfileAdmin)
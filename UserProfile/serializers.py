from rest_framework import serializers
from UserProfile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Profile
        fields = [
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
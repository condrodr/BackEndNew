from django.shortcuts import render
from rest_framework import viewsets
from UserProfile.models import Profile
from django_filters import rest_framework as filters
from UserProfile.serializers import ProfileSerializer
# Create your views here.

class UserProfileFilter(filters.FilterSet):
    timestamp = filters.DateFromToRangeFilter()
   
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

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UserProfileFilter
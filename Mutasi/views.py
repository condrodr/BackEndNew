from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import NotaMutasiKeluarCart, TerimaMutasiCart, DetailMutasiKeluarCart
from .serializers import NotaMutasiKeluarCartSerializer, TerimaMutasiCartSerializer, DetailMutasiKeluarCartSerializer

class NotaMutasiKeluarCartFilter(filters.FilterSet):
    tanggal_nota = filters.DateFromToRangeFilter()
    jatuh_tempo_nota = filters.DateFromToRangeFilter()
   
    class Meta:
        model = NotaMutasiKeluarCart
        fields = ['id',
            'perusahaan_kantor',
            'divisi_kantor',
            'gudang_awal',
            'tujuan_kirim',
            'nama_pengirim',
            'no_kendaraan',
            'tanggal_mutasi',
            'no_mutasi',
            'jenis_mutasi',
            'status_kiriman',
            'nilai_mutasi',
            'keterangan_mutasi',
        ]

class NotaMutasiKeluarCartView(viewsets.ModelViewSet):
    queryset = NotaMutasiKeluarCart.objects.all()
    serializer_class = NotaMutasiKeluarCartSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = NotaMutasiKeluarCartFilter

class TerimaMutasiCartFilter(filters.FilterSet):
    tanggal_diterima = filters.DateFromToRangeFilter()
   
    class Meta:
        model = TerimaMutasiCart
        fields = ['id',
            'nama_penerima',
            'no_mutasi',
            'jenis_mutasi',
            'tanggal_diterima',
            'status_penerimaan',
            'keterangan_penerimaan',
        ]

class TerimaMutasiCartView(viewsets.ModelViewSet):
    queryset = TerimaMutasiCart.objects.all()
    serializer_class = TerimaMutasiCartSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TerimaMutasiCartFilter

class DetailMutasiKeluarCartFilter(filters.FilterSet):
    tanggal_diterima = filters.DateFromToRangeFilter()
   
    class Meta:
        model = DetailMutasiKeluarCart
        fields = ['id',
            'id',
            'kode_produk',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order',
            'tanggal_mutasi',
            'harga_modal_pcs',
            'no_mutasi',
            'id_detail_mutasi',
        ]

class DetailMutasiKeluarCartView(viewsets.ModelViewSet):
    queryset = DetailMutasiKeluarCart.objects.all()
    serializer_class = DetailMutasiKeluarCartSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailMutasiKeluarCartFilter

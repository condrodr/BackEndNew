from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from SuratJalanKeluar.models import SJKeluar, DetailSJKeluar, DetailLokasiKeluarProduk
from SuratJalanKeluar.serializers import SJKeluarSerializer, DetailSJKeluarSerializer, DetailLokasiKeluarProdukSerializer

class SJKeluarFilter(filters.FilterSet):
    timestamp = filters.DateFromToRangeFilter()
    class Meta:
        model = SJKeluar
        fields = ['id','no_nota_keluar','no_SJ_keluar','no_kendaraan','nama_pengirim',
                'timestamp','gudang_awal','tujuan_kirim','jenis_sj_keluar','status_kiriman'
        ]
class SJKeluarView(viewsets.ModelViewSet):
    queryset = SJKeluar.objects.all()
    serializer_class = SJKeluarSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SJKeluarFilter

class DetailSJKeluarFilter(filters.FilterSet):
    timestamp = filters.DateFromToRangeFilter()
    jumlah_order = filters.BaseRangeFilter(
        field_name='jumlah_order',lookup_expr='range'
    )
    harga_beli_produk = filters.BaseRangeFilter(
        field_name='harga_beli_produk',lookup_expr='range'
    )
    class Meta:
        model = DetailSJKeluar
        fields = ['id','id_detailSJK','no_nota_keluar','no_SJ_keluar','nama_produk',
                'kode_produk','kemasan_produk','jumlah_order','harga_beli_produk'
        ]

class DetailSJKeluarView(viewsets.ModelViewSet):
    queryset = DetailSJKeluar.objects.all()
    serializer_class = DetailSJKeluarSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailSJKeluarFilter

class DetailLokasiKeluarProdukView(viewsets.ModelViewSet):
    queryset = DetailLokasiKeluarProduk.objects.all()
    serializer_class = DetailLokasiKeluarProdukSerializer


from django.shortcuts import render

from rest_framework import viewsets
from SuratJalanMasuk.models import SJMasuk, DetailSJMasuk
from django_filters import rest_framework as filters
from SuratJalanMasuk.serializers import SJMasukSerializer, DetailSJMasukSerializer

class SJMasukFilter(filters.FilterSet):
  
    timestamp = filters.DateFromToRangeFilter()
   
    class Meta:
        model = SJMasuk
        fields = ['no_SJ_masuk','no_nota_masuk','no_kendaraan','nama_pembawa',
                'asal_kiriman','timestamp','gudang_cabang','status_barang','nama_penerima',
                'jenis_sj_masuk','modal_SJ_masuk'
        ]

class SJMasukView(viewsets.ModelViewSet):
    queryset = SJMasuk.objects.all()
    serializer_class = SJMasukSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SJMasukFilter

class DetailSJMasukFilter(filters.FilterSet):
    timestamp = filters.DateFromToRangeFilter()
   
    class Meta:
        model = DetailSJMasuk
        fields = [
            'id_detailSJM',
            'no_SJ_masuk',
            'no_nota_masuk',
            'id_detail_nota_masuk',
            'nama_produk',
            'kode_produk',
            'jumlah_order',
            'kemasan_produk',
            'asal_kiriman',
            'jenis_sj_masuk',
            'timestamp',
            'harga_beli_pcs',
        ]

class DetailSJMasukView(viewsets.ModelViewSet):
    queryset = DetailSJMasuk.objects.all()
    serializer_class = DetailSJMasukSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailSJMasukFilter

from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from ReturBarang.models import NotaRetur, DetailRetur
from ReturBarang.serializers import NotaReturSerializer, DetailReturSerailizer
# Create your views here.

class NotaReturFilter(filters.FilterSet):
   
    class Meta:
        model = NotaRetur
        fields = [
            'no_nota_retur',
            'no_SJ_retur',
            'no_nota_jual',
            'tanggal_retur',
            'nilai_nota_retur',
            'gudang_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
        ]

class NotaReturView(viewsets.ModelViewSet):
    queryset = NotaRetur.objects.all()
    serializer_class = NotaReturSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = NotaReturFilter


class DetailReturFilter(filters.FilterSet):
   
    class Meta:
        model = DetailRetur
        fields = [
            'no_nota_retur',
            'no_SJ_retur',
            'no_nota_jual',
            'nama_produk',
            'kode_produk',
            'kemasan_produk',
            'jumlah_barang',
            'harga_jual',
            'harga_beli',
            'kondisi_barang',
            'id_detail_nota_jual'

        ]
class DetailReturView(viewsets.ModelViewSet):
    queryset = DetailRetur.objects.all()
    serializer_class = DetailReturSerailizer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailReturFilter
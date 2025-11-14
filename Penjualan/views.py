from django.shortcuts import render
from rest_framework import viewsets
from Penjualan.models import NotaPenjualan, DetailPenjualan
from Penjualan.serializers import NotaPenjualanSerializer, DetailPenjualanSerializer
from django_filters import rest_framework as filters
# Create your views here.
class NotaPenjualanFilter(filters.FilterSet):
    tanggal_nota = filters.DateFromToRangeFilter()
    jatuh_tempo_nota = filters.DateFromToRangeFilter()
   
    class Meta:
        model = NotaPenjualan
        fields = ['tanggal_nota','jatuh_tempo_nota','nama_outlet','no_nota_jual',
                'jenis_faktur','jenis_penjualan','kantor_cabang','nama_salesman',
                'status_nota','status_barang','divisi_kantor','perusahaan_kantor',
                'nilai_nota_jual','piutang_standing' 
        ]
class NotaPenjualanView(viewsets.ModelViewSet):
    queryset = NotaPenjualan.objects.all()
    serializer_class = NotaPenjualanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = NotaPenjualanFilter

class DetailPenjualanFilter(filters.FilterSet):
    tanggal_nota = filters.DateFromToRangeFilter()

    harga_jual_pcs = filters.BaseRangeFilter(
        field_name='harga_jual_pcs',lookup_expr='range'
    )
    jumlah_order = filters.BaseRangeFilter(
        field_name='jumlah_order',lookup_expr='range'
    )
    
    class Meta:
        model = DetailPenjualan
        fields = ['no_nota_jual','nama_produk','kemasan_produk',
                'jumlah_order','harga_jual_pcs','discount_produk','tanggal_nota'
        ]

class DetailPenjualanView(viewsets.ModelViewSet):
    queryset = DetailPenjualan.objects.all()
    serializer_class = DetailPenjualanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailPenjualanFilter
    

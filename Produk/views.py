from django.shortcuts import render
from rest_framework import viewsets
from Produk.models import Produk, ProdukPromotion
from django_filters import rest_framework as filters
from Produk.serializers import ProdukPromotionSerailizer, ProdukSerailizer
# Create your views here.

class ProdukFilter(filters.FilterSet):
    timestamp = filters.DateTimeFromToRangeFilter()
    harga_HET_pcs = filters.BaseRangeFilter(
        field_name='harga_HET_pcs',lookup_expr='range'
    )
    harga_HTO_pcs = filters.BaseRangeFilter(
        field_name='harga_HTO_pcs',lookup_expr='range'
    )
    class Meta:
        model = Produk
        fields = ['nama_produk','kode_produk','kemasan_produk','isi_per_pack','volume_per_pcs','merek_produk','submerek_produk',
                'tiersegmen_produk','usersegmen_produk','timestamp','harga_HET_pcs','harga_HTO_pcs','divisi_kantor',
                'kategori_produk','jenis_produk','spek_produk','fungsi_produk','produsen_produk'
                ]

class ProdukView(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerailizer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProdukFilter

class ProdukPromotionView(viewsets.ModelViewSet):
    queryset = ProdukPromotion.objects.all()
    serializer_class = ProdukPromotionSerailizer
    
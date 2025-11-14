from django.shortcuts import render
from rest_framework import viewsets
from Pembelian.serializers import NotaPembelianSerializer, DetailPembelianSerializer
from Pembelian.models import NotaPembelian, DetailPembelian
from django_filters import rest_framework as filters
# Create your views here.

class NotaPembelianFilter(filters.FilterSet):
    tanggal_nota_beli = filters.DateFromToRangeFilter()
    jatuh_tempo_beli = filters.DateFromToRangeFilter()
   
    class Meta:
        model = NotaPembelian
        fields = [ 
            'id',
            'no_nota_beli',
            'supplier',
            'gudang_cabang',
            'faktur_atau_tidak',
            'hutang_standing',
            'diorder_oleh',
            'nilai_nota_beli',
            'tanggal_nota_beli',
            'jatuh_tempo_beli',
            'status_nota_beli',
            'status_barang_beli',
            'divisi_kantor',
            'perusahaan_kantor',
            'total_volume_nota',
            'cluster_pembeli',
        ]

class NotaPembelianView(viewsets.ModelViewSet):
    queryset = NotaPembelian.objects.all()
    serializer_class = NotaPembelianSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = NotaPembelianFilter

class DetailPembelianFilter(filters.FilterSet):
    
    class Meta:
        model = DetailPembelian
        fields = [ 
            'id',
            'id_detail_nota_masuk',
            'no_nota_beli',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order_beli',
            'harga_beli_pcs',
            'kantor_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
            'supplier'
        ]

class DetailPembelianView(viewsets.ModelViewSet):
    queryset = DetailPembelian.objects.all()
    serializer_class = DetailPembelianSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailPembelianFilter
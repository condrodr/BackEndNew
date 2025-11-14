from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from Stok.serializers import StokSerializer, KartuStokSerializer, StokTransitSerializer, LokasiStokSerializer, SelisihBongkarMuatSerializer
from Stok.models import StokUtama, StokTransit, LokasiStok, SelisihBongkarMuat, KartuStok
# Create your views here.

class StokUtamaFilter(filters.FilterSet):
  
    timestamp = filters.DateFromToRangeFilter()
   
    class Meta:
        model = StokUtama
        fields = ['id','nama_produk','kode_produk','jumlah_barang','gudang_cabang',
                'detail_lokasi','timestamp','harga_beli_weighted','divisi_kantor',
                'perusahaan_kantor'
        ]


class StokView(viewsets.ModelViewSet):
    queryset = StokUtama.objects.all()
    serializer_class = StokSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StokUtamaFilter

class StokTransitFilter(filters.FilterSet):
  
    timestamp = filters.DateFromToRangeFilter()
   
    class Meta:
        model = StokTransit
        fields = [ 'id',
            'no_nota_transit',
            'no_SJ_keluar',
            'nama_produk',
            'kode_produk',
            'timestamp',
            'harga_modal_pcs',
            'jumlah_barang',
            'tujuan_kirim',
            'jenis_transit',
            'gudang_cabang',
            'divisi_kantor',
            'perusahaan_kantor',]

class StokTransitView(viewsets.ModelViewSet):
    queryset = StokTransit.objects.all()
    serializer_class = StokTransitSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StokTransitFilter

class LokasiStokFilter(filters.FilterSet):
   
    class Meta:
        model = LokasiStok
        fields = [ 'id',
            'nama_lokasi',
            'gudang_cabang',
            'jenis_lokasi',
            'perusahaan_kantor',

            ]

class LokasiStokView(viewsets.ModelViewSet):
    queryset = LokasiStok.objects.all()
    serializer_class = LokasiStokSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LokasiStokFilter


class SelisihBongkarMuatFilter(filters.FilterSet):
  
    timestamp = filters.DateFromToRangeFilter()
   
    class Meta:
        model = SelisihBongkarMuat
        fields = [ 'id',
            'id_sj_transaksi',
            'id_ks_transaksi',
            'jenis_transaksi',
            'nama_produk',
            'kode_produk',
            'jumlah_selisih',
            'timestamp',
            'keterangan',
            'gudang_cabang',
            'jumlah_selisih',
            'divisi_kantor',
            'perusahaan_kantor',
            'status_selisih',
        ]

class SelisihBongkarMuatView(viewsets.ModelViewSet):
    queryset = SelisihBongkarMuat.objects.all()
    serializer_class = SelisihBongkarMuatSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SelisihBongkarMuatFilter

class KartuStokFilter(filters.FilterSet):
  
    timestamp = filters.DateFromToRangeFilter()
   
    class Meta:
        model = KartuStok
        fields = [ 'id',
            'nama_produk',
            'kode_produk',
            'tahun_produksi_produk',
            'id_ks_transaksi',
            'id_sj_transaksi',
            'jenis_transaksi',
            'detail_lokasi',
            'gudang_cabang',
            'jumlah_transaksi' ,
            'estimasi_harga_beli',
            'stok_awal',
            'stok_akhir',
            'timestamp',
            'keterangan',
            'divisi_kantor',
            'perusahaan_kantor' 
        ]


class KartuStokView(viewsets.ModelViewSet):
    queryset = KartuStok.objects.all()
    serializer_class = KartuStokSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = KartuStokFilter
    

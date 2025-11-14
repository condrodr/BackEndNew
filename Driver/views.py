from django.shortcuts import render
from Driver.models import Driver, PlanKiriman, DetailPlanKiriman, UpdateNotaKirimSebagian, DetailSisaNotaTerkirimSebagian
from Driver.serializers import DriverSerializer, PlanKirimanSerializer,  DetailPlanKirimanSerializer, UpdateNotaKirimSebagianSerializer, DetailSisaNotaTerkirimSebagianSerializer
from rest_framework import viewsets
from django.db.models import Q
from django_filters import rest_framework as filters
# Create your views here.

class DriverFilter(filters.FilterSet):
    class Meta:
        model = Driver
        fields = ['no_kendaraan','nama_supir','jenis_kendaraan','status_kendaraan',
                'tarif_rupiah_per_km','max_berat','max_dus','max_rupiah'
        ]

class DriverView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DriverFilter

class PlanKirimanFilter(filters.FilterSet):
    tanggal_kiriman = filters.DateFromToRangeFilter()
    #start_kerja = filters.DateFromToRangeFilter()
    selesai_kerja = filters.DateFromToRangeFilter()
    start_kerja = filters.CharFilter(method='filter_start_kerja')
    def filter_start_kerja(self, queryset, name, value):
        if value.lower() == "null":  # ✅ Jika user mengirim "null", ubah ke nilai None
            return queryset.filter(Q(start_kerja__isnull=True))
        return queryset.filter(**{name: value})  # ✅ Jika tidak, filter biasa
    
    def filter_selesai_kerja(self, queryset, name, value):
        if value.lower() == "null":  # ✅ Jika user mengirim "null", ubah ke nilai None
            return queryset.filter(Q(selesai_kerja__isnull=True))
        return queryset.filter(**{name: value})  # ✅ Jika tidak, filter biasa
   
    class Meta:
        model = PlanKiriman
        fields = ['no_kendaraan','id_plan_kiriman','nomer_urut_kiriman','tanggal_kiriman',
                'nama_supir','total_jarak_km','biaya_kiriman','start_kerja',
                'selesai_kerja','ada_returan','keterangan_retur'
        ]

class PlanKirimanView(viewsets.ModelViewSet):
    queryset = PlanKiriman.objects.all()
    serializer_class = PlanKirimanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PlanKirimanFilter

class DetailPlanKirimanFilter(filters.FilterSet):
    class Meta:
        model = DetailPlanKiriman
        fields = ['no_nota_keluar','no_sj_keluar','jenis_transaksi','nama_tujuan_kiriman',
                'GPS_lokasi_kiriman','no_urut_kiriman','id_plan_kiriman','id_detail_plan_kiriman'
        ]

class DetailPlanKirimanView(viewsets.ModelViewSet):
    queryset = DetailPlanKiriman.objects.all()
    serializer_class = DetailPlanKirimanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailPlanKirimanFilter

class UpdateNotaKirimSebagianFilter(filters.FilterSet):
    terakhir_terkirim = filters.CharFilter(method='filter_terakhir_terkirim')

    def filter_terakhir_terkirim(self, queryset, name, value):
        if value.lower() == "null":  # ✅ Jika user mengirim "null", ubah ke nilai None
            return queryset.filter(Q(terakhir_terkirim__isnull=True))
        return queryset.filter(**{name: value})  # ✅ Jika tidak, filter biasa
    class Meta:
        model = UpdateNotaKirimSebagian
        fields = ['no_nota_keluar','tujuan_kirim','nilai_belum_terkirim','terakhir_terkirim',
                'status_kiriman'
        ]

class UpdateNotaKirimSebagianView(viewsets.ModelViewSet):
    queryset = UpdateNotaKirimSebagian.objects.all()
    serializer_class = UpdateNotaKirimSebagianSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UpdateNotaKirimSebagianFilter

class DetailSisaNotaTerkirimSebagianFilter(filters.FilterSet):
    class Meta:
        model = DetailSisaNotaTerkirimSebagian
        fields = ['no_nota_keluar','id_detail_nota','tujuan_kirim','nama_produk',
                'kemasan_produk','jumlah_produk','harga_jual_pcs', 'discount_produk',
                'subtotal_vol','jumlah_order_terkirim'
        ]

class DetailSisaNotaTerkirimSebagianView(viewsets.ModelViewSet):
    queryset = DetailSisaNotaTerkirimSebagian.objects.all()
    serializer_class = DetailSisaNotaTerkirimSebagianSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DetailSisaNotaTerkirimSebagianFilter
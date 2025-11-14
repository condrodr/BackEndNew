from django.shortcuts import render
from Customer.serializers import RegisteredCustomerSerializer, LoyaltyPointCustomerSerializer, DataPotensiCustomerSerializer, DailyRegisteredCustomerReportSerializer, KontrakOutletPromotionSerializer, DaftarPromosiBerjalanSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from Customer.models import RegisteredCustomer, LoyaltyPointCustomer, DataPotensiCustomer, DailyRegisteredCustomerReport, KontrakOutletPromotion, DaftarPromosiBerjalan
# Create your views here.
class RegisteredCustomerFilter(filters.FilterSet):
    timestamp = filters.DateTimeFromToRangeFilter()
    jumlah_pekerja = filters.LookupChoiceFilter(field_name='jumlah_pekerja',lookup_choices=[
        ('exact','Equals'),
        ('gt','Greater than'),
        ('lt','Less than'),
        ('gte','Greater than or equal to'),
        ('lte','Less than or equal to')
    ])
    plafon_outlet = filters.LookupChoiceFilter(field_name='plafon_outlet',lookup_choices=[
        ('exact','Equals'),
        ('gt','Greater than'),
        ('lt','Less than'),
        ('gte','Greater than or equal to'),
        ('lte','Less than or equal to')
    ])
    discount_level_outlet = filters.LookupChoiceFilter(field_name='discount_level_outlet',lookup_choices=[
        ('exact','Equals'),
        ('gt','Greater than'),
        ('lt','Less than'),
        ('gte','Greater than or equal to'),
        ('lte','Less than or equal to')
    ])
    
    class Meta:
        model = RegisteredCustomer
        fields = ['tipe_outlet','kategori_outlet','cluster_outlet','divisi_kantor','perusahaan_kantor',
                'kecamatan_outlet','kabupaten_outlet','provinsi_outlet','kelurahan_outlet','nama_salesman',
                'jumlah_pekerja','rute_kunjungan','level_outlet','plafon_outlet','discount_level_outlet',
                'nama_outlet','kode_outlet','kode_prinsipal_outlet'
                ]

class RegisteredCustomerView(viewsets.ModelViewSet):
    queryset = RegisteredCustomer.objects.all()
    serializer_class = RegisteredCustomerSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = RegisteredCustomerFilter

class LoyaltyPointCustomerView(viewsets.ModelViewSet):
    queryset = LoyaltyPointCustomer.objects.all()
    serializer_class = LoyaltyPointCustomerSerializer

class DataPotensiCustomerView(viewsets.ModelViewSet):
    queryset = DataPotensiCustomer.objects.all()
    serializer_class = DataPotensiCustomerSerializer

class DailyRegisteredCustomerReportView(viewsets.ModelViewSet):
    queryset = DailyRegisteredCustomerReport.objects.all()
    serializer_class = DailyRegisteredCustomerReportSerializer

class KontrakOutletPromotionView(viewsets.ModelViewSet):
    queryset = KontrakOutletPromotion.objects.all()
    serializer_class = KontrakOutletPromotionSerializer

class DaftarPromosiBerjalanFilter(filters.FilterSet):
    tanggal_nota = filters.DateFromToRangeFilter()
    jatuh_tempo_nota = filters.DateFromToRangeFilter()
   
    class Meta:
        model = DaftarPromosiBerjalan
        fields = ['nama_promo','tipe_promo','pembuat_promo','alias_promo' 
        ]
class DaftarPromosiBerjalanView(viewsets.ModelViewSet):
    queryset = DaftarPromosiBerjalan.objects.all()
    serializer_class = DaftarPromosiBerjalanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DaftarPromosiBerjalanFilter
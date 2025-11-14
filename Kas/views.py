from django.shortcuts import render
from Kas.models import AkunPembukuan
from Kas.serializers import AkunPembukuanSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
# Create your views here.

class AkunPembukuanFilter(filters.FilterSet):
    class Meta:
        model = AkunPembukuan
        fields = ['nama_akun','kode_akun','tipe_akun'
        ]

class AkunPembukuanView(viewsets.ModelViewSet):
    queryset = AkunPembukuan.objects.all()
    serializer_class = AkunPembukuanSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AkunPembukuanFilter

# class JournalEntryFilter(filters.FilterSet):
#     class Meta:
#         model = JournalEntry
#         fields = [
#              'id',
#             'kategori_action',
#             'detaildeskripsi',
#             'timestamp',
#             'kode_entry',
#             'validitas'
#         ]

# class JournalEntryView(viewsets.ModelViewSet):
#     queryset = JournalEntry.objects.all()
#     serializer_class = JournalEntrySerializer
#     filter_backends = [filters.DjangoFilterBackend]
#     filterset_class = JournalEntryFilter

# class JournalEntryLineFilter(filters.FilterSet):
#     class Meta:
#         model = JournalEntryLine
#         fields = [
#             'id',
#             'kode_entry',
#             'nama_akun',
#             'kode_akun',
#             'date',
#             'tipe_journal',
#             'value_transaksi'
#         ]

# class JournalEntryLineView(viewsets.ModelViewSet):
#     queryset = JournalEntryLine.objects.all()
#     serializer_class = JournalEntryLineSerializer
#     filter_backends = [filters.DjangoFilterBackend]
#     filterset_class = JournalEntryLineFilter

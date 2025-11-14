from django.shortcuts import render
from django_filters import rest_framework as filters
from LedgerKas.models import Kas, MasterAkun, JournalEntryLine, JournalEntry
from LedgerKas.serializers import KasSerializer, MasterAkunSerializer, JournalEntrySerializer, JournalEntryLineSerializer
from rest_framework import viewsets
# Create your views here.

class KasFilter(filters.FilterSet):
    class Meta:
        model = Kas
        fields = [
                    'tanggal_kas',
                    'keluar_masuk',
                    'bentuk_kas',
                    'detail_kas',
                    'jenis_transaksi',
                    'keterangan_transaksi',
                    'nilai_transaksi',
                    'transaction_id',
                    'perusahaan_kantor'
        ]


class KasView(viewsets.ModelViewSet):
    queryset = Kas.objects.all()
    serializer_class = KasSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = KasFilter

class MasterAkunFilter(filters.FilterSet):
    class Meta:
        model = MasterAkun
        fields = [
            'kode_akun',
            'nama_akun',
            'kategori',
            'sub_kategori'
        ]


class MasterAkunView(viewsets.ModelViewSet):
    queryset = MasterAkun.objects.all()
    serializer_class = MasterAkunSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = MasterAkunFilter

# class TabelNeracaAwalView(viewsets.ModelViewSet):
#     queryset = TabelNeracaAwal.objects.all()
#     serializer_class = TabelNeracaAwalSerializer

# class JurnalEntryView(viewsets.ModelViewSet):
#     queryset = JurnalEntry.objects.all()
#     serializer_class = JurnalEntrySerializer
class JournalEntryFilter(filters.FilterSet):
    class Meta:
        model = JournalEntry
        fields = [
             'id',
            'kategori_action',
            'detaildeskripsi',
            'timestamp',
            'kode_entry',
            'validitas'
        ]

class JournalEntryView(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = JournalEntryFilter

class JournalEntryLineFilter(filters.FilterSet):
    class Meta:
        model = JournalEntryLine
        fields = [
            'id',
            'kode_entry',
            'nama_akun',
            'kode_akun',
            'date',
            'tipe_journal',
            'value_transaksi'
        ]

class JournalEntryLineView(viewsets.ModelViewSet):
    queryset = JournalEntryLine.objects.all()
    serializer_class = JournalEntryLineSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = JournalEntryLineFilter
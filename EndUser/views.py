from django.shortcuts import render
from django_filters import rest_framework as filters
from EndUser.models import JualanRekomender, RewardSpinWheel, Rekomender, RewardList
from EndUser.serializers import JualanRekomenderSerializer, RewardSpinWheelSerializer, RekomenderSerializer, RewardListSerializer
from rest_framework import viewsets

# Create your views here.

class JualanRekomenderFilter(filters.FilterSet):
    class Meta:
        model = JualanRekomender
        fields = [
                    'id',
                    'id_rekomender',
                    'rekomender',
                    'dms_rekomender',
                    'produk_dijual',
                    'jumlah_produk',
                    'nama_pembeli',
                    'no_telp_pembeli',
                    'tanggal'
        ]


class JualanRekomenderView(viewsets.ModelViewSet):
    queryset = JualanRekomender.objects.all()
    serializer_class = JualanRekomenderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = JualanRekomenderFilter

class RewardSpinWheelFilter(filters.FilterSet):
    class Meta:
        model = RewardSpinWheel
        fields = [
                    'id',
                    'id_reward',
                    'kode_dms',
                    'nama_reward',
        ]


class RewardSpinWheelView(viewsets.ModelViewSet):
    queryset = RewardSpinWheel.objects.all()
    serializer_class = RewardSpinWheelSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = RewardSpinWheelFilter

class RekomenderFilter(filters.FilterSet):
    class Meta:
        model = Rekomender
        fields = [
                    'id',
                    'id_rekomender',
                    'nama_rekomender',
                    'dms_rekomender',
                    'kode_outlet',
                    'budget_per_liter'
        ]


class RekomenderView(viewsets.ModelViewSet):
    queryset = Rekomender.objects.all()
    serializer_class = RekomenderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = RekomenderFilter

class RewardListFilter(filters.FilterSet):
    class Meta:
        model = RewardList
        fields = [
                    'id',
                    'kode_dms',
                    'probabilitas',
                    'nama_barang',
                    'jumlah_barang',
                   
        ]


class RewardListView(viewsets.ModelViewSet):
    queryset = RewardList.objects.all()
    serializer_class = RewardListSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = RewardListFilter
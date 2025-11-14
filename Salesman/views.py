from django.shortcuts import render
from rest_framework import viewsets
from Salesman.serializers import SalesmanSerializer, CatatanSalesmanSerializer
from Salesman.models import Salesman, CatatanSalesman
# Create your views here.

class SalesmanView(viewsets.ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer

class CatatanSalesmanView(viewsets.ModelViewSet):
    queryset = CatatanSalesman.objects.all()
    serializer_class = CatatanSalesmanSerializer
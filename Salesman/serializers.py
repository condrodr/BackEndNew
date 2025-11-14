from rest_framework import serializers
from Salesman.models import Salesman, CatatanSalesman

class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = (
            'nama_sales',
            'target_minimum',
            'kas_disales',
            'target_incentive',
        )

class CatatanSalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatatanSalesman
        fields = (
            'nama_sales',
            'tugas_ke_sales',
            'catatan_ke_sales',
            'info_dari_sales',
            'timestamp',
        )
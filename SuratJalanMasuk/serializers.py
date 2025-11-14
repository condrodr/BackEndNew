# produk/serializers.py

from rest_framework import serializers
from SuratJalanMasuk.models import SJMasuk, DetailSJMasuk

class SJMasukSerializer(serializers.ModelSerializer):
    class Meta:
        model = SJMasuk
        fields = [
            'id',
            'no_SJ_masuk',
            'no_nota_masuk',
            'no_kendaraan',
            'nama_pembawa',
            'asal_kiriman',
            'status_barang',
            'timestamp',
            'gudang_cabang',
            'nama_penerima',
            'jenis_sj_masuk',
            'modal_SJ_masuk',
        ]

class DetailSJMasukSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSJMasuk
        fields = [
            'id',
            'id_detailSJM',
            'no_SJ_masuk',
            'no_nota_masuk',
            'id_detail_nota_masuk',
            'nama_produk',
            'kode_produk',
            'jumlah_order',
            'kemasan_produk',
            'asal_kiriman',
            'jenis_sj_masuk',
            'timestamp',
            'harga_beli_pcs',
        ]

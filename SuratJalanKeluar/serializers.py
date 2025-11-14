# produk/serializers.py

from rest_framework import serializers
from SuratJalanKeluar.models import SJKeluar, DetailSJKeluar, DetailLokasiKeluarProduk

class SJKeluarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SJKeluar
        fields = [
            'id',
            'no_nota_keluar',
            'no_SJ_keluar',
            'no_kendaraan',
            'nama_pengirim',
            'timestamp',
            'gudang_awal',
            'tujuan_kirim',
            'jenis_sj_keluar',
            'status_kiriman',
            'modal_SJ_keluar',
        ]

class DetailSJKeluarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSJKeluar
        fields = [
            'id',
            'nama_produk',
            'kode_produk',
            'jumlah_order',
            'kemasan_produk',
            'no_nota_keluar',
            'no_SJ_keluar',
            'id_detailSJK',
            'tujuan_kirim',
            'harga_beli_produk',
        ]

class DetailLokasiKeluarProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailLokasiKeluarProduk
        fields = [
            'id',
            'no_nota_keluar',
            'no_SJ_keluar',
            'kode_keluar_produk',
            'nama_produk',
            'kode_produk',
            'jumlah_produk',
            'harga_modal_produk',
            'kemasan_produk',
            'gudang_awal',
            'lokasi_produk',
        ]

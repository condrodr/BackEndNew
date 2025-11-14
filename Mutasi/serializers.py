from rest_framework import serializers
from .models import NotaMutasiKeluarCart, TerimaMutasiCart, DetailMutasiKeluarCart

class NotaMutasiKeluarCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaMutasiKeluarCart
        fields = (
            'id',
            'perusahaan_kantor',
            'divisi_kantor',
            'gudang_awal',
            'tujuan_kirim',
            'nama_pengirim',
            'no_kendaraan',
            'tanggal_mutasi',
            'no_mutasi',
            'jenis_mutasi',
            'status_kiriman',
            'nilai_mutasi',
            'keterangan_mutasi',
        )

class TerimaMutasiCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerimaMutasiCart
        fields = (
            'id',
            'nama_penerima',
            'no_mutasi',
            'jenis_mutasi',
            'tanggal_diterima',
            'status_penerimaan',
            'keterangan_penerimaan',
        )

class DetailMutasiKeluarCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailMutasiKeluarCart
        fields = (
            'id',
            'kode_produk',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order',
            'tanggal_mutasi',
            'harga_modal_pcs',
            'no_mutasi',
            'id_detail_mutasi',
        )

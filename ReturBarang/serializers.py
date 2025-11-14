from rest_framework import serializers
from ReturBarang.models import NotaRetur, DetailRetur

class NotaReturSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaRetur
        fields = (
            'no_nota_retur',
            'no_SJ_retur',
            'no_nota_jual',
            'tanggal_retur',
            'nilai_nota_retur',
            'perusahaan_kantor',
            'gudang_cabang',
            'divisi_kantor'
        )

class DetailReturSerailizer(serializers.ModelSerializer):
    class Meta:
        model = DetailRetur
        fields = (
           'no_nota_retur',
            'no_SJ_retur',
            'no_nota_jual',
            'id_detail_nota_jual',
            'nama_produk',
            'kode_produk',
            'kemasan_produk',
            'jumlah_barang',
            'harga_jual',
            'harga_beli',
            'kondisi_barang'
        )
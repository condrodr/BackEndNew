from rest_framework import serializers
from Penjualan.models import NotaPenjualan, DetailPenjualan

class NotaPenjualanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaPenjualan
        fields = (
            'id',
            'nama_outlet',
            'kode_outlet',
            'no_nota_jual',
            
            'jenis_penjualan',
            'jenis_faktur',
            'nilai_nota_jual',
            'piutang_standing',
            'kantor_cabang',
            'nama_salesman',
            'status_nota',
            'status_barang',
            'tanggal_nota',
            'jatuh_tempo_nota',
            'divisi_kantor',
            'perusahaan_kantor',
        )


class DetailPenjualanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPenjualan
        fields = (
            'id',
            'no_nota_jual',
            'nama_produk',
            'kemasan_produk',
            'jumlah_order',
            'harga_jual_pcs',
            'discount_produk',
            'kode_outlet',
            
            'subtotal_vol',
            'tanggal_nota',
        )
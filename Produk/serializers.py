from rest_framework import serializers
from Produk.models import Produk, ProdukPromotion

class ProdukSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = (
            'id',
            'nama_produk',
            'alias_produk',
            'kode_produk',
            'kimap_produk',
            'photo_produk_1',
            'kemasan_produk',
            'isi_per_pack',
            'volume_per_pcs',
            'deskripsi_produk',
            'fungsi_produk',
            'harga_HET_pcs',
            'harga_HTO_pcs',
            'harga_beli_per_pack',
            'merek_produk',
            'submerek_produk',
            'tiersegmen_produk',
            'usersegmen_produk',
            'submerek_produk',
            'perusahaan_kantor',
        )

class ProdukPromotionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = ProdukPromotion
        fields = (
            'nama_promo',
            'tipe_promo',
            'yang_dipromokan',
            'status_promo',
            'deskripsi_promo',
            'diskon_promo',
            'dimulai_tanggal',
            'berakhir_tanggal',
           
        )
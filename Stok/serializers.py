from rest_framework import serializers
from Stok.models import StokUtama, StokTransit, LokasiStok, SelisihBongkarMuat, KartuStok

class StokSerializer(serializers.ModelSerializer):
    class Meta:
        model = StokUtama
        fields = (
            'id',
            'nama_produk',
            'kode_produk',
            'jumlah_barang',
            'gudang_cabang',
            'divisi_kantor',
            'detail_lokasi',
            'perusahaan_kantor',
            
            
        )

class StokTransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StokTransit
        fields = (
            'id',
            'no_nota_transit',
            'no_SJ_keluar',
            'nama_produk',
            'kode_produk',
            'timestamp',
            'harga_modal_pcs',
            'jumlah_barang',
            'tujuan_kirim',
            'jenis_transit',
            'gudang_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
        )

class KartuStokSerializer(serializers.ModelSerializer):
    class Meta:
        model = KartuStok
        fields = (
            'id',
            'nama_produk',
            'kode_produk',
            'tahun_produksi_produk',
            'id_ks_transaksi',
            'id_sj_transaksi',
            'jenis_transaksi',
            'detail_lokasi',
            'gudang_cabang',
            'jumlah_transaksi' ,
            'estimasi_harga_beli',
            'stok_awal',
            'stok_akhir',
            'timestamp',
            'keterangan',
            'divisi_kantor',
            'perusahaan_kantor' 
            
        )

class LokasiStokSerializer(serializers.ModelSerializer):
    class Meta:
        model = LokasiStok
        fields = (
            'id',
            'nama_lokasi',
            'deskripsi_lokasi',
            'foto_lokasi',
            'gudang_cabang',
            'divisi_kantor',
            'perusahaan_kantor',
            'jenis_lokasi'
            
        )

class SelisihBongkarMuatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelisihBongkarMuat
        fields = (
            'id',
            'id_sj_transaksi',
            'id_ks_transaksi',
            'jenis_transaksi',
            'nama_produk',
            'kode_produk',
            'jumlah_selisih',
            'timestamp',
            'keterangan',
            'gudang_cabang',
            'jumlah_selisih',
            'divisi_kantor',
            'perusahaan_kantor',
            'status_selisih',
            
        )
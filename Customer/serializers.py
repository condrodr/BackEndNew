from rest_framework import serializers
from .models import RegisteredCustomer, LoyaltyPointCustomer, DataPotensiCustomer, DailyRegisteredCustomerReport, KontrakOutletPromotion, DaftarPromosiBerjalan

class RegisteredCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredCustomer
        fields = (
            'id',
            'nama_outlet',
            'no_telepon_outlet',
            'no_telepon_lain_outlet',
            'kode_outlet',
            'kode_prinsipal_outlet',
            'photo_tampak_depan',
            'level_outlet',
            'tipe_outlet',
            'deskripsi_outlet',
            'no_KTP_outlet',
            'photo_ktp_pemilik',
            'no_NPWP_outlet',
            'discount_level_outlet',
            'jumlah_pekerja',
            'GPS_lokasi_outlet',
            'Google_Place_ID',
            'alamat_outlet',
            'kelurahan_outlet',
            'kecamatan_outlet',
            'kabupaten_outlet',
            'provinsi_outlet',
            'nama_salesman',
            'cluster_outlet',
            'rute_kunjungan',
            'nama_pemilik',
            'plafon_outlet'
        )


class LoyaltyPointCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyPointCustomer
        fields = (
            'kode_outlet',
            'tipe_transaksi',
            'loyalty_point',
            'loyalty_transaction_id'
        )

class DataPotensiCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPotensiCustomer
        fields = (
            'nama_outlet',
            'kode_potensi_customer',
            'kode_prinsipal_outlet',
            'GPS_lokasi_outlet',
            'Google_Place_ID',
            'nama_pemilik',
            'no_telepon_outlet',
            'kondisi_outlet',
            'jumlah_pekerja',
            'urgency_outlet'
        )

class DailyRegisteredCustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRegisteredCustomerReport
        fields = (
            'kode_outlet',
            'timestamp',
            'update_kondisi_outlet',
            'update_merek_kompetitor',
            'alasan_belum_order',
            'update_pesaing',
            'update_kondisi_outlet',
            'estimasi_jumlah_stok_terlihat'
        )
        
class KontrakOutletPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = KontrakOutletPromotion
        fields = (
            'id',
            'nama_promo',
            # 'tipe_promo',
            # 'yang_dipromokan',
            'kode_outlet',
            'status_promo',
            # 'deskripsi_promo',
            'target_promo',
            'dimulai_tanggal',
            'berakhir_tanggal'
        )

class DaftarPromosiBerjalanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaftarPromosiBerjalan
        fields = '__all__'
    
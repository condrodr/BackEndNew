from rest_framework import serializers
from LedgerKas.models import Kas, MasterAkun, JournalEntry, JournalEntryLine

class KasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kas
        fields = (
            'tanggal_kas',
            'keluar_masuk',
            'bentuk_kas',
            'detail_kas',
            'jenis_transaksi',
            'keterangan_transaksi',
            'nilai_transaksi',
            'transaction_id',
            'perusahaan_kantor'
        )

class MasterAkunSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterAkun
        fields = (
            'kode_akun',
            'nama_akun',
            'kategori',
            'sub_kategori'
        )

# class TabelNeracaAwalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TabelNeracaAwal
#         fields = (
#             'kode_akun',
#             'nama_akun',
#             'kategori',
#             'jenis_data',
#             'saldo_awal'
#         )

# class JurnalEntrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JurnalEntry
#         fields = (
#             'keterangan',
#             'debit_kredit',
#             'nama_akun',
#             'kode_akun',
#             'kategori',
#             'sub_kategori',
#             'nominal',
#         )

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = (
            'id',
            'kategori_action',
            'detaildeskripsi',
            'timestamp',
            'kode_entry',
            'validitas'
        )


class JournalEntryLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntryLine
        fields = (
            'id',
            'kode_entry',
            'nama_akun',
            'kode_akun',
            'date',
            'tipe_journal',
            'value_transaksi'

        )
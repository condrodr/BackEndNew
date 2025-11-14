from rest_framework import serializers
from Kas.models import AkunPembukuan

class AkunPembukuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AkunPembukuan
        fields = (
            'id',
            'nama_akun',
            'kode_akun',
            'tipe_akun'
          
        )

# class JournalEntrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JournalEntry
#         fields = (
#             'id',
#             'kategori_action',
#             'detaildeskripsi',
#             'timestamp',
#             'kode_entry',
#             'validitas'
#         )


# class JournalEntryLineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JournalEntryLine
#         fields = (
#             'id',
#             'kode_entry',
#             'nama_akun',
#             'kode_akun',
#             'date',
#             'tipe_journal',
#             'value_transaksi'

#         )

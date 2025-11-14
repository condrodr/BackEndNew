from rest_framework import serializers
from .models import Rekomender, JualanRekomender, RewardSpinWheel, RewardList


class RekomenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rekomender
        fields = "__all__"


class RewardSpinWheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardSpinWheel
        fields = "__all__"


class JualanRekomenderSerializer(serializers.ModelSerializer):
    # pastikan read-only & (opsional) set format tampilan
    # tanggal = serializers.DateField(read_only=True, format="%Y-%m-%d")
    # kalau mau ada versi tampilan Indonesia juga:
    #tanggal_display = serializers.DateField(source="tanggal", read_only=True, format="%d/%m/%Y")
    class Meta:
        model = JualanRekomender
        fields = "__all__"

class RewardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RewardList
        fields = "__all__"

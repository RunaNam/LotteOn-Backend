from rest_framework import serializers
from .models import Allergy, Etc


class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'content',
            'checked',
        )
        model = Allergy


class EtcSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'content',
            'checked',
        )
        model = Etc

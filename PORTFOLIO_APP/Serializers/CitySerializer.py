from rest_framework import serializers
from ..Models import CityModel


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'
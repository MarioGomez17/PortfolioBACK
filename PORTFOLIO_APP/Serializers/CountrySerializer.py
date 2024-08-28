from rest_framework import serializers
from ..Models import CountryModel


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'
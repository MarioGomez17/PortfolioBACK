from rest_framework import serializers
from ..Models import CompanyModel
from .CitySerializer import CitySerializer


class CompanySerializer(serializers.ModelSerializer):
    City_Company = CitySerializer(read_only=True)

    class Meta:
        model = CompanyModel
        fields = ['Id_Company', 'Name_Company', 'Boss_Company', 'City_Company']

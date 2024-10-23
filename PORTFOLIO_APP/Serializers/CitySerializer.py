from rest_framework import serializers
from ..Models import CityModel
from .DepartmentSerializer import DepartmentSerializer

class CitySerializer(serializers.ModelSerializer):
    Department_City = DepartmentSerializer(read_only=True)
    class Meta:
        model = CityModel
        fields = ['Id_City', 'Name_City', 'UrlMaps_City', 'Department_City']
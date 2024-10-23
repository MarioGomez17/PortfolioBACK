from rest_framework import serializers
from ..Models import DepartmentModel
from .CountrySerializer import CountrySerializer

class DepartmentSerializer(serializers.ModelSerializer):
    Country_Department = CountrySerializer(read_only=True)
    class Meta:
        model = DepartmentModel
        fields = ['Id_Department', 'Name_Department', 'Country_Department']
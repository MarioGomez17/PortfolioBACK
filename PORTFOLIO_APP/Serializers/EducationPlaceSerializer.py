from rest_framework import serializers
from ..Models import EducationPlaceModel


class EducationPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationPlaceModel
        fields = ['Id_EducationPlace', 'Name_EducationPlace']
    
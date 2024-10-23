from rest_framework import serializers
from ..Models import EducationTypeModel


class EducationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationTypeModel
        fields = ['Id_EducationType', 'Name_EducationType']
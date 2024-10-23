from rest_framework import serializers
from ..Models import AcademyModel


class AcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademyModel
        fields = ['Id_Academy', 'Name_Academy']
    
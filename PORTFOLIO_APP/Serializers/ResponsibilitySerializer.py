from rest_framework import serializers
from ..Models import ResponsibilityModel


class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsibilityModel
        fields = ['Id_Responsibility', 'Description_Responsibility']
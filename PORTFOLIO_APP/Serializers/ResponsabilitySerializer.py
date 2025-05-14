from rest_framework import serializers
from ..Models import ResponsabilityModel


class ResponsabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsabilityModel
        fields = ['Id_Responsability', 'Description_Responsability']
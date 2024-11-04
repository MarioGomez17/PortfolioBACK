from rest_framework import serializers
from ..Models import DivisionModel


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionModel
        fields = ['Id_Division', 'Name_Division']
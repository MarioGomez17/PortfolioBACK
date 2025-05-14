from rest_framework import serializers
from ..Models import ControlVersionModel


class ControlVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlVersionModel
        fields = ['Id_ControlVersion', 'Name_ControlVersion']
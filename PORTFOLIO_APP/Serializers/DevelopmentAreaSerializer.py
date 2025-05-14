from rest_framework import serializers
from ..Models import DevelopmentAreaModel


class DevelopmentAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentAreaModel
        fields = ['Id_DevelopmentArea', 'Name_DevelopmentArea']
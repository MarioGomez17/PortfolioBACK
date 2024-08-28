from rest_framework import serializers
from ..Models import DivisionModel


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionModel
        fields = '__all__'
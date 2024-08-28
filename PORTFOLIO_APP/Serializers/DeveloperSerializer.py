from rest_framework import serializers
from ..Models import DeveloperModel


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperModel
        fields = '__all__'
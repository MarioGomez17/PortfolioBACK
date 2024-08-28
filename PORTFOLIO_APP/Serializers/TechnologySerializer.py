from rest_framework import serializers
from ..Models import TechnologyModel


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyModel
        fields = '__all__'
from rest_framework import serializers
from ..Models import ProgrammingLanguageModel


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguageModel
        fields = '__all__'
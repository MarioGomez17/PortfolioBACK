from rest_framework import serializers
from ..Models import ProgrammingLanguageModel
from .TechnologySerializer import TechnologySerializer


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    Technologies_ProgrammingLanguage = TechnologySerializer(read_only=True, many=True)
    class Meta:
        model = ProgrammingLanguageModel
        fields = ['Id_ProgrammingLanguage', 'Name_ProgrammingLanguage', 'Logo_ProgrammingLanguage', 'Technologies_ProgrammingLanguage']
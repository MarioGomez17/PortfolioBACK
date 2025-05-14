from rest_framework import serializers
from ..Models import ProgrammingLanguageModel
from .DevelopmentAreaSerializer import DevelopmentAreaSerializer


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    DevelopmentArea_ProgrammingLanguage = DevelopmentAreaSerializer(read_only=True)

    class Meta:
        model = ProgrammingLanguageModel
        fields = ['Id_ProgrammingLanguage', 'Name_ProgrammingLanguage', 'Description_ProgrammingLanguage',
                  'Logo_ProgrammingLanguage', 'DevelopmentArea_ProgrammingLanguage']

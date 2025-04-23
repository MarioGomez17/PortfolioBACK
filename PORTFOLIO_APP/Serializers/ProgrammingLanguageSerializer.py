from rest_framework import serializers
from ..Models import ProgrammingLanguageModel

class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguageModel
        fields = ['Id_ProgrammingLanguage', 'Name_ProgrammingLanguage', 'Description_ProgrammingLanguage', 'Logo_ProgrammingLanguage']
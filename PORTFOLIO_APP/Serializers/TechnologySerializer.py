from rest_framework import serializers
from ..Models import TechnologyModel
from .DevelopmentAreaSerializer import DevelopmentAreaSerializer
from .ProgrammingLanguageSerializer import ProgrammingLanguageSerializer


class TechnologySerializer(serializers.ModelSerializer):
    DevelopmentArea_Technology = DevelopmentAreaSerializer(read_only=True)
    ProgrammingLanguage_Technology = ProgrammingLanguageSerializer(
        read_only=True)

    class Meta:
        model = TechnologyModel
        fields = ['Id_Technology', 'Name_Technology', 'Description_Technology',
                  'Logo_Technology', 'DevelopmentArea_Technology', 'ProgrammingLanguage_Technology']

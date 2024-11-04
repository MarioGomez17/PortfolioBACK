from rest_framework import serializers
from ..Models import TechnologyModel
from .DivisionSerializer import DivisionSerializer
from .ProgrammingLanguageSerializer import ProgrammingLanguageSerializer

class TechnologySerializer(serializers.ModelSerializer):
    Division_Technology = DivisionSerializer(read_only=True)
    ProgrammingLanguage_Technology = ProgrammingLanguageSerializer(read_only=True)
    class Meta:
        model = TechnologyModel
        fields = ['Id_Technology', 'Name_Technology', 'Logo_Technology', 'Division_Technology', 'ProgrammingLanguage_Technology']
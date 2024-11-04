from rest_framework import serializers
from ..Models import DeveloperModel
from .CitySerializer import CitySerializer
from .TechnologySerializer import TechnologySerializer
from .LanguageSerializer import LanguageSerializer
from .EducationSerializer import EducationSerializer

class DeveloperSerializer(serializers.ModelSerializer):
    City_Developer = CitySerializer(read_only=True)
    Technologies_Developer = TechnologySerializer(many=True, read_only=True)
    Languages_Developer = LanguageSerializer(many=True, read_only=True)
    Education_Developer = EducationSerializer(many=True, read_only=True)
    class Meta:
        model = DeveloperModel
        fields = ['Id_Developer', 'Name_Developer', 'LastName_Developer', 'Email_Developer', 'Phone_Developer', 'LinkedinName_Developer', 'LinkedinUrl_Developer', 'GitHubName_Developer', 'GitHubUrl_Developer', 'City_Developer', 'Description_Developer', 'Technologies_Developer', 'Languages_Developer', 'Education_Developer']

from rest_framework import serializers
from ..Models import DeveloperModel
from .CitySerializer import CitySerializer
from .ProgrammingLanguageSerializer import ProgrammingLanguageSerializer
from .TechnologySerializer import TechnologySerializer
from .LanguageSerializer import LanguageSerializer
from .EducationSerializer import EducationSerializer
from .SkillSerializer import SkillSerializer
from .ProjectSerializer import ProjectSerializer
from .ExperienceSerializer import ExperienceSerializer
from .IdeAndToolSerializer import IdeAndToolSerializer
from .ControlVersionSerializer import ControlVersionSerializer
from .ContactInformationSerializer import ContactInformationSerializer


class DeveloperSerializer(serializers.ModelSerializer):
    City_Developer = CitySerializer(read_only=True)
    Technologies_Developer = TechnologySerializer(many=True, read_only=True)
    ProgrammingLanguages_Developer = ProgrammingLanguageSerializer(
        many=True, read_only=True)
    Languages_Developer = LanguageSerializer(many=True, read_only=True)
    Education_Developer = EducationSerializer(many=True, read_only=True)
    Skills_Developer = SkillSerializer(many=True, read_only=True)
    Projects_Developer = ProjectSerializer(many=True, read_only=True)
    Experience_Developer = ExperienceSerializer(many=True, read_only=True)
    IdesAndTools_Developer = IdeAndToolSerializer(many=True, read_only=True)
    ControlsVersionDeveloper = ControlVersionSerializer(
        many=True, read_only=True)
    ContactsInformation_Developer = ContactInformationSerializer(
        many=True, read_only=True)

    class Meta:
        model = DeveloperModel
        fields = ['Id_Developer', 'Name_Developer', 'LastName_Developer', 'Email_Developer', 'Phone_Developer', 'LinkedinName_Developer', 'LinkedinUrl_Developer', 'GitHubName_Developer', 'GitHubUrl_Developer', 'Role_Developer', 'ShortProfile_Developer',
                  'LongProfile_Developer', 'City_Developer', 'ProgrammingLanguages_Developer', 'Technologies_Developer', 'IdesAndTools_Developer', 'ControlsVersionDeveloper', 'Skills_Developer', 'Languages_Developer', 'Education_Developer', 'Projects_Developer', 'Experience_Developer', 'ContactsInformation_Developer']

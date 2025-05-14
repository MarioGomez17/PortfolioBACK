from rest_framework import serializers
from ..Models import EducationModel
from .AcademySerializer import AcademySerializer
from .EducationTypeSerializer import EducationTypeSerializer
from .EducationPlaceSerializer import EducationPlaceSerializer
from .EducationAchievementSerializer import EducationAchievementSerializer


class EducationSerializer(serializers.ModelSerializer):
    Academy_Education = AcademySerializer(read_only=True)
    EducationType_Education = EducationTypeSerializer(read_only=True)
    EducationPlace_Education = EducationPlaceSerializer(read_only=True)
    Achievements_Education = EducationAchievementSerializer(
        many=True, read_only=True)

    class Meta:
        model = EducationModel
        fields = ['Id_Education', 'DegreeName_Education', 'Description_Education', 'Date_Education', 'DegreeFile_Education',
                  'Academy_Education', 'EducationType_Education', 'EducationPlace_Education', 'Achievements_Education']

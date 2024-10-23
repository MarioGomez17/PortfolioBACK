from rest_framework import serializers
from ..Models import EducationModel
from .AcademySerializer import AcademySerializer
from .EducationTypeSerializer import EducationTypeSerializer


class EducationSerializer(serializers.ModelSerializer):
    Academy_Education = AcademySerializer(read_only=True)
    EducationType_Education = EducationTypeSerializer(read_only=True)

    class Meta:
        model = EducationModel
        fields = ['Id_Education', 'DegreeName_Education', 'DegreeFile_Education',
                'Academy_Education', 'EducationType_Education']

from rest_framework import serializers
from ..Models import ExperienceModel
from .RoleSerializer import RoleSerializer
from .CompanySerializer import CompanySerializer
from .ResponsabilitySerializer import ResponsabilitySerializer
from .AchievementSerializer import AchievementSerializer


class ExperienceSerializer(serializers.ModelSerializer):
    Role_Experience = RoleSerializer(read_only=True)
    Company_Experience = CompanySerializer(read_only=True)
    Experience_Responsibilities = ResponsabilitySerializer(many=True, read_only=True)
    Experience_Achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = ExperienceModel
        fields = ['Id_Experience', 'Description_Experience', 'DateStart_Experience', 'DateEnd_Experience', 'Role_Experience', 'Company_Experience', 'Experience_Responsibilities', 'Experience_Achievements']

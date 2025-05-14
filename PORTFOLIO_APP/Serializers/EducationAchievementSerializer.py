from rest_framework import serializers
from ..Models import EducationAchievementModel


class EducationAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationAchievementModel
        fields = ['Id_EducationAchievement', 'Description_EducationAchievement']
    
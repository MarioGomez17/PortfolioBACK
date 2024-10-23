from rest_framework import serializers
from ..Models import SkillModel


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = ['Id_Skill', 'Name_Skill']
from rest_framework import serializers
from ..Models import TechnologyModel
from .SkillSerializer import SkillSerializer

class TechnologySerializer(serializers.ModelSerializer):
    Skill_Technology = SkillSerializer(read_only=True)
    class Meta:
        model = TechnologyModel
        fields = ['Id_Technology', 'Name_Technology', 'Logo_Technology', 'Skill_Technology']
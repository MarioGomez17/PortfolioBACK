from rest_framework import serializers
from ..Models import ProjectModel
from .TechnologySerializer import TechnologySerializer

class ProjectSerializer(serializers.ModelSerializer):
    Technologies_Project = TechnologySerializer(many=True, read_only=True)
    class Meta:
        model = ProjectModel
        fields = ['Id_Project', 'Name_Project', 'Description_Project', 'URL_Project', 'Technologies_Project']
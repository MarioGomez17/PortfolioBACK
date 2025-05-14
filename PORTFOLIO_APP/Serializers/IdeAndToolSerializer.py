from rest_framework import serializers
from ..Models import IdeAndToolModel


class IdeAndToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeAndToolModel
        fields = ['Id_IdeAndTool', 'Name_IdeAndTool']
from rest_framework import serializers
from ..Models import LanguageModel


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = ['Id_Language', 'Name_Language', 'Level_Language']
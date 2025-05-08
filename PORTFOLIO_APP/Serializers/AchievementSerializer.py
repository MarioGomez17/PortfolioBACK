from rest_framework import serializers
from ..Models import AchievementModel


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementModel
        fields = ['Id_Achievement', 'Description_Achievement']

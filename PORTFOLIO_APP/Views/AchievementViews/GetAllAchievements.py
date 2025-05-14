from rest_framework import generics
from ...Models.AchievementModel import AchievementModel
from ...Serializers.AchievementSerializer import AchievementSerializer


class AchievementsGetView(generics.ListAPIView):
    queryset = AchievementModel.objects.all()
    serializer_class = AchievementSerializer

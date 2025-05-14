from rest_framework import generics
from ...Models.AchievementModel import AchievementModel
from ...Serializers.AchievementSerializer import AchievementSerializer


class AchievementGetView(generics.RetrieveAPIView):
    queryset = AchievementModel.objects.all()
    serializer_class = AchievementSerializer

from rest_framework import generics
from ...Models.AchievementModel import AchievementModel
from ...Serializers.AchievementSerializer import AchievementSerializer


class AchievementDeleteView(generics.DestroyAPIView):
    queryset = AchievementModel.objects.all()
    serializer_class = AchievementSerializer
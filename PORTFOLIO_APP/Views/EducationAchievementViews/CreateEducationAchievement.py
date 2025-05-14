from rest_framework import generics
from ...Models.EducationAchievementModel import EducationAchievementModel
from ...Serializers.EducationAchievementSerializer import EducationAchievementSerializer


class EducationAchievementCreateView(generics.CreateAPIView):
    queryset = EducationAchievementModel.objects.all()
    serializer_class = EducationAchievementSerializer
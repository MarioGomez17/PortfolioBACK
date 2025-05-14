from rest_framework import generics
from ...Models.EducationAchievementModel import EducationAchievementModel
from ...Serializers.EducationAchievementSerializer import EducationAchievementSerializer


class EducationAchievementUpdateView(generics.UpdateAPIView):
    queryset = EducationAchievementModel.objects.all()
    serializer_class = EducationAchievementSerializer
from rest_framework import generics
from ...Models.SkillModel import SkillModel
from ...Serializers.SkillSerializer import SkillSerializer


class SkillUpdateView(generics.UpdateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
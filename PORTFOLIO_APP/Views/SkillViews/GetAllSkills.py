from rest_framework import viewsets, generics
from ...Models.SkillModel import SkillModel
from ...Serializers.SkillSerializer import SkillSerializer


class SkillsGetView(generics.ListAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer

from rest_framework import viewsets, generics
from ...Models.SkillModel import SkillModel
from ...Serializers.SkillSerializer import SkillSerializer


class SkillGetView(generics.RetrieveAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer

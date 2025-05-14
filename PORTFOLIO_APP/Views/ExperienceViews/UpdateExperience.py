from rest_framework import generics
from ...Models.ExperienceModel import ExperienceModel
from ...Serializers.ExperienceSerializer import ExperienceSerializer


class ExperienceUpdateView(generics.UpdateAPIView):
    queryset = ExperienceModel.objects.all()
    serializer_class = ExperienceSerializer

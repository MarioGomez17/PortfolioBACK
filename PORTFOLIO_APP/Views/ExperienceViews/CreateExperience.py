from rest_framework import generics
from ...Models.ExperienceModel import ExperienceModel
from ...Serializers.ExperienceSerializer import ExperienceSerializer


class ExperienceCreateView(generics.CreateAPIView):
    queryset = ExperienceModel.objects.all()
    serializer_class = ExperienceSerializer
from rest_framework import generics
from ...Models.EducationModel import EducationModel
from ...Serializers.EducationSerializer import EducationSerializer


class EducationCreateView(generics.CreateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializer
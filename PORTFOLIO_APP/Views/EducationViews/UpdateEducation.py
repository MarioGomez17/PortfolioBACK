from rest_framework import generics
from ...Models.EducationModel import EducationModel
from ...Serializers.EducationSerializer import EducationSerializer


class EducationUpdateView(generics.UpdateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializer

from rest_framework import generics
from ...Models.EducationPlaceModel import EducationPlaceModel
from ...Serializers.EducationPlaceSerializer import EducationPlaceSerializer


class EducationPlaceUpdateView(generics.UpdateAPIView):
    queryset = EducationPlaceModel.objects.all()
    serializer_class = EducationPlaceSerializer

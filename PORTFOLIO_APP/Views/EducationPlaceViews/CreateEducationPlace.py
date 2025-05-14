from rest_framework import generics
from ...Models.EducationPlaceModel import EducationPlaceModel
from ...Serializers.EducationPlaceSerializer import EducationPlaceSerializer


class EducationPlaceCreateView(generics.CreateAPIView):
    queryset = EducationPlaceModel.objects.all()
    serializer_class = EducationPlaceSerializer
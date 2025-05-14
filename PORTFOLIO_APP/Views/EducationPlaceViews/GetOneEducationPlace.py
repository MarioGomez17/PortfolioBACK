from rest_framework import generics
from ...Models.EducationPlaceModel import EducationPlaceModel
from ...Serializers.EducationPlaceSerializer import EducationPlaceSerializer


class EducationPlaceGetView(generics.RetrieveAPIView):
    queryset = EducationPlaceModel.objects.all()
    serializer_class = EducationPlaceSerializer

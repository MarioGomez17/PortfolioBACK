from rest_framework import generics
from ...Models.EducationTypeModel import EducationTypeModel
from ...Serializers.EducationTypeSerializer import EducationTypeSerializer


class EducationTypeCreateView(generics.CreateAPIView):
    queryset = EducationTypeModel.objects.all()
    serializer_class = EducationTypeSerializer
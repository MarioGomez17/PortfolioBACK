from rest_framework import generics
from ...Models.EducationTypeModel import EducationTypeModel
from ...Serializers.EducationTypeSerializer import EducationTypeSerializer


class EducationTypeUpdateView(generics.UpdateAPIView):
    queryset = EducationTypeModel.objects.all()
    serializer_class = EducationTypeSerializer

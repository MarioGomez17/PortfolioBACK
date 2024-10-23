from rest_framework import viewsets, generics
from ...Models.EducationTypeModel import EducationTypeModel
from ...Serializers.EducationTypeSerializer import EducationTypeSerializer


class EducationTypeGetView(generics.RetrieveAPIView):
    queryset = EducationTypeModel.objects.all()
    serializer_class = EducationTypeSerializer

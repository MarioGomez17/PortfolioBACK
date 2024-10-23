from rest_framework import viewsets, generics
from ...Models.EducationTypeModel import EducationTypeModel
from ...Serializers.EducationTypeSerializer import EducationTypeSerializer


class EducationTypesGetView(generics.ListAPIView):
    queryset = EducationTypeModel.objects.all()
    serializer_class = EducationTypeSerializer

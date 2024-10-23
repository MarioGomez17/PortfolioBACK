from rest_framework import viewsets, generics
from ...Models.AcademyModel import AcademyModel
from ...Serializers.AcademySerializer import AcademySerializer


class AcademiesGetView(generics.ListAPIView):
    queryset = AcademyModel.objects.all()
    serializer_class = AcademySerializer
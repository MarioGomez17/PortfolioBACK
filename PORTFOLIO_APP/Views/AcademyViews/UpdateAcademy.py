from rest_framework import generics
from ...Models.AcademyModel import AcademyModel
from ...Serializers.AcademySerializer import AcademySerializer


class AcademyUpdateView(generics.UpdateAPIView):
    queryset = AcademyModel.objects.all()
    serializer_class = AcademySerializer

from rest_framework import generics
from ...Models.AcademyModel import AcademyModel
from ...Serializers.AcademySerializer import AcademySerializer


class AcademyGetView(generics.RetrieveAPIView):
    queryset = AcademyModel.objects.all()
    serializer_class = AcademySerializer

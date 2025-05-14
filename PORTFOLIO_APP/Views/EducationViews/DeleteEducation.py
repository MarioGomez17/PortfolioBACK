from rest_framework import generics
from ...Models.EducationModel import EducationModel
from ...Serializers.EducationSerializer import EducationSerializer


class EducationDeleteView(generics.DestroyAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializer
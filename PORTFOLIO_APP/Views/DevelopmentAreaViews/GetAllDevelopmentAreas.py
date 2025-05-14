from rest_framework import generics
from ...Models.DevelopmentAreaModel import DevelopmentAreaModel
from ...Serializers.DevelopmentAreaSerializer import DevelopmentAreaSerializer


class DevelopmentAreasGetView(generics.ListAPIView):
    queryset = DevelopmentAreaModel.objects.all()
    serializer_class = DevelopmentAreaSerializer

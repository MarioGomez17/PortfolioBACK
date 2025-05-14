from rest_framework import generics
from ...Models.DevelopmentAreaModel import DevelopmentAreaModel
from ...Serializers.DevelopmentAreaSerializer import DevelopmentAreaSerializer


class DevelopmentAreaUpdateView(generics.UpdateAPIView):
    queryset = DevelopmentAreaModel.objects.all()
    serializer_class = DevelopmentAreaSerializer
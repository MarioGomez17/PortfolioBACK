from rest_framework import generics
from ...Models.DevelopmentAreaModel import DevelopmentAreaModel
from ...Serializers.DevelopmentAreaSerializer import DevelopmentAreaSerializer


class DevelopmentAreaCreateView(generics.CreateAPIView):
    queryset = DevelopmentAreaModel.objects.all()
    serializer_class = DevelopmentAreaSerializer
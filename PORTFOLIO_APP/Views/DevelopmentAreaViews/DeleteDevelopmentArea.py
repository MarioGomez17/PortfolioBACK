from rest_framework import generics
from ...Models.DevelopmentAreaModel import DevelopmentAreaModel
from ...Serializers.DevelopmentAreaSerializer import DevelopmentAreaSerializer


class DevelopmentAreaDeleteView(generics.DestroyAPIView):
    queryset = DevelopmentAreaModel.objects.all()
    serializer_class = DevelopmentAreaSerializer
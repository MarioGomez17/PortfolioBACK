from rest_framework import generics
from ...Models.DevelopmentAreaModel import DevelopmentAreaModel
from ...Serializers.DevelopmentAreaSerializer import DevelopmentAreaSerializer


class DevelopmentAreaGetView(generics.RetrieveAPIView):
    queryset = DevelopmentAreaModel.objects.all()
    serializer_class = DevelopmentAreaSerializer

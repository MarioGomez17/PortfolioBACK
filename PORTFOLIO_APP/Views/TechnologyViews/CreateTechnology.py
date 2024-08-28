from rest_framework import viewsets, generics
from ...Models.TechnologyModel import TechnologyModel
from ...Serializers.TechnologySerializer import TechnologySerializer


class TechnologyCreateView(generics.CreateAPIView):
    queryset = TechnologyModel.objects.all()
    serializer_class = TechnologySerializer

from rest_framework import generics
from ...Models.TechnologyModel import TechnologyModel
from ...Serializers.TechnologySerializer import TechnologySerializer


class TechnologiesGetView(generics.ListAPIView):
    queryset = TechnologyModel.objects.all()
    serializer_class = TechnologySerializer

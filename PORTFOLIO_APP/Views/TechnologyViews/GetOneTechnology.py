from rest_framework import generics
from ...Models.TechnologyModel import TechnologyModel
from ...Serializers.TechnologySerializer import TechnologySerializer


class TechnologyGetView(generics.RetrieveAPIView):
    queryset = TechnologyModel.objects.all()
    serializer_class = TechnologySerializer

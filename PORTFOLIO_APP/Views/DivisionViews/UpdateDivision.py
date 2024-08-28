from rest_framework import viewsets, generics
from ...Models.DivisionModel import DivisionModel
from ...Serializers.DivisionSerializer import DivisionSerializer


class DivisionUpdateView(generics.UpdateAPIView):
    queryset = DivisionModel.objects.all()
    serializer_class = DivisionSerializer
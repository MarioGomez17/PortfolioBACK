from rest_framework import generics
from ...Models.IdeAndToolModel import IdeAndToolModel
from ...Serializers.IdeAndToolSerializer import IdeAndToolSerializer


class IdesAndToolsGetView(generics.ListAPIView):
    queryset = IdeAndToolModel.objects.all()
    serializer_class = IdeAndToolSerializer

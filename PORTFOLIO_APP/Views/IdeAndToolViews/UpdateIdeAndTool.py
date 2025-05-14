from rest_framework import generics
from ...Models.IdeAndToolModel import IdeAndToolModel
from ...Serializers.IdeAndToolSerializer import IdeAndToolSerializer


class IdeAndToolUpdateView(generics.UpdateAPIView):
    queryset = IdeAndToolModel.objects.all()
    serializer_class = IdeAndToolSerializer

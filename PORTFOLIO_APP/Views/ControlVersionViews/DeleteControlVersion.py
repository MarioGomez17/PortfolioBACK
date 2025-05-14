from rest_framework import generics
from ...Models.ControlVersionModel import ControlVersionModel
from ...Serializers.ControlVersionSerializer import ControlVersionSerializer


class ControlVersionDeleteView(generics.DestroyAPIView):
    queryset = ControlVersionModel.objects.all()
    serializer_class = ControlVersionSerializer
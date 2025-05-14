from rest_framework import generics
from ...Models.ControlVersionModel import ControlVersionModel
from ...Serializers.ControlVersionSerializer import ControlVersionSerializer


class ControlVersionCreateView(generics.CreateAPIView):
    queryset = ControlVersionModel.objects.all()
    serializer_class = ControlVersionSerializer
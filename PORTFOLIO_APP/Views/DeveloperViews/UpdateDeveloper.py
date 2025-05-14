from rest_framework import generics
from ...Models.DeveloperModel import DeveloperModel
from ...Serializers.DeveloperSerializer import DeveloperSerializer


class DeveloperUpdateView(generics.UpdateAPIView):
    queryset = DeveloperModel.objects.all()
    serializer_class = DeveloperSerializer
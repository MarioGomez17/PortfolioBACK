from rest_framework import generics
from ...Models.DeveloperModel import DeveloperModel
from ...Serializers.DeveloperSerializer import DeveloperSerializer


class DeveloperDeleteView(generics.DestroyAPIView):
    queryset = DeveloperModel.objects.all()
    serializer_class = DeveloperSerializer
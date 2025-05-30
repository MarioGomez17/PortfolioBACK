from rest_framework import generics
from ...Models.DeveloperModel import DeveloperModel
from ...Serializers.DeveloperSerializer import DeveloperSerializer


class DevelopersGetView(generics.ListAPIView):
    queryset = DeveloperModel.objects.all()
    serializer_class = DeveloperSerializer

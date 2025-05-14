from rest_framework import generics
from ...Models.ResponsabilityModel import ResponsabilityModel
from ...Serializers.ResponsabilitySerializer import ResponsabilitySerializer


class ResponsabilityUpdateView(generics.UpdateAPIView):
    queryset = ResponsabilityModel.objects.all()
    serializer_class = ResponsabilitySerializer

from rest_framework import generics
from ...Models.ResponsabilityModel import ResponsabilityModel
from ...Serializers.ResponsabilitySerializer import ResponsabilitySerializer


class ResponsabilitiesGetView(generics.ListAPIView):
    queryset = ResponsabilityModel.objects.all()
    serializer_class = ResponsabilitySerializer

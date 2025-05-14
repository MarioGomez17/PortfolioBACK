from rest_framework import generics
from ...Models.ResponsabilityModel import ResponsabilityModel
from ...Serializers.ResponsabilitySerializer import ResponsabilitySerializer


class ResponsabilityGetView(generics.RetrieveAPIView):
    queryset = ResponsabilityModel.objects.all()
    serializer_class = ResponsabilitySerializer

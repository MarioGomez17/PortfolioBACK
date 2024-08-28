from rest_framework import viewsets, generics
from ...Models.CityModel import CityModel
from ...Serializers.CitySerializer import CitySerializer


class CityGetView(generics.RetrieveAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer
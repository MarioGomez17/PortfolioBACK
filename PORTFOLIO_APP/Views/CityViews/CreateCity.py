from rest_framework import generics
from ...Models.CityModel import CityModel
from ...Serializers.CitySerializer import CitySerializer


class CityCreateView(generics.CreateAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer
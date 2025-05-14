from rest_framework import generics
from ...Models.CityModel import CityModel
from ...Serializers.CitySerializer import CitySerializer


class CitiesGetView(generics.ListAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer

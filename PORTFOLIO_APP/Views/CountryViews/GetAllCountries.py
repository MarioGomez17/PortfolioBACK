from rest_framework import generics
from ...Models.CountryModel import CountryModel
from ...Serializers.CountrySerializer import CountrySerializer


class CountriesGetView(generics.ListAPIView):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer

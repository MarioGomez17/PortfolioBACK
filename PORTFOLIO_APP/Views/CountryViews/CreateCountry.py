from rest_framework import viewsets, generics
from ...Models.CountryModel import CountryModel
from ...Serializers.CountrySerializer import CountrySerializer


class CountryCreateView(generics.CreateAPIView):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer
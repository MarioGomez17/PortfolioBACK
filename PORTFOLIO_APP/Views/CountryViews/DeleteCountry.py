from rest_framework import viewsets, generics
from ...Models.CountryModel import CountryModel
from ...Serializers.CountrySerializer import CountrySerializer


class CountryDeleteView(generics.DestroyAPIView):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer
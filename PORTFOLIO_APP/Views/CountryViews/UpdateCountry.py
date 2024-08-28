from rest_framework import viewsets, generics
from ...Models.CountryModel import CountryModel
from ...Serializers.CountrySerializer import CountrySerializer


class CountryUpdateView(generics.UpdateAPIView):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer
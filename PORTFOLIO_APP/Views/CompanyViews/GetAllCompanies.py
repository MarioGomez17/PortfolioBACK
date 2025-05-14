from rest_framework import generics
from ...Models.CompanyModel import CompanyModel
from ...Serializers.CompanySerializer import CompanySerializer


class CompaniesGetView(generics.ListAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

from rest_framework import generics
from ...Models.CompanyModel import CompanyModel
from ...Serializers.CompanySerializer import CompanySerializer


class CompanyGetView(generics.RetrieveAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

from rest_framework import generics
from ...Models.ContactInformationModel import ContactInformationModel
from ...Serializers.ContactInformationSerializer import ContactInformationSerializer


class ContactInformationDeleteView(generics.DestroyAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer
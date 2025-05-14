from rest_framework import generics
from ...Models.ContactInformationModel import ContactInformationModel
from ...Serializers.ContactInformationSerializer import ContactInformationSerializer


class ContactInformationUpdateView(generics.UpdateAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer

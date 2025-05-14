from rest_framework import serializers
from ..Models import ContactInformationModel


class ContactInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInformationModel
        fields = ['Id_ContactInformation', 'PersonName_ContactInformation', 'PersonEmail_ContactInformation', 'PersonPhone_ContactInformation',
                  'Subject_ContactInformation', 'BudgetRange_ContactInformation', 'Message_ContactInformation', 'ContactMethod_ContactInformation']

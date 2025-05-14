from django.urls import path
from ..Views.ContactInformationViews.CreateContactInformation import ContactInformationCreateView
from ..Views.ContactInformationViews.DeleteContactInformation import ContactInformationDeleteView
from ..Views.ContactInformationViews.GetAllContactsInformation import ContactsInformationGetView
from ..Views.ContactInformationViews.GetOneContactInformation import ContactInformationGetView
from ..Views.ContactInformationViews.UpdateContactInformation import ContactInformationUpdateView


urlpatterns = [
    path('ContactInformation/create/', ContactInformationCreateView.as_view(), name='Create Contact Information'),
    path('ContactInformation/<int:pk>/delete/', ContactInformationDeleteView.as_view(), name='Delete Contact Information'),
    path('ContactInformations/', ContactsInformationGetView.as_view(), name='Contact Informations List'),
    path('ContactInformation/<int:pk>/', ContactInformationGetView.as_view(), name='Contact Information Detail'),
    path('ContactInformation/<int:pk>/update/', ContactInformationUpdateView.as_view(), name='Update Contact Information'),
]
from django.urls import path
from ..Views.CountryViews.CreateCountry import CountryCreateView
from ..Views.CountryViews.DeleteCountry import CountryDeleteView
from ..Views.CountryViews.GetAllCountries import CountriesGetView
from ..Views.CountryViews.GetOneCountry import CountryGetView
from ..Views.CountryViews.UpdateCountry import CountryUpdateView


urlpatterns = [
    path('Country/create/', CountryCreateView.as_view(), name='Create Country'),
    path('Country/<int:pk>/delete/', CountryDeleteView.as_view(), name='Delete Country'),
    path('Countries/', CountriesGetView.as_view(), name='Countries List'),
    path('Country/<int:pk>/', CountryGetView.as_view(), name='Country Detail'),
    path('Country/<int:pk>/update/', CountryUpdateView.as_view(), name='Update Country'),
]
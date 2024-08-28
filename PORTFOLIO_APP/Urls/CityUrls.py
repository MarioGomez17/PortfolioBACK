from django.urls import path
from ..Views.CityViews.CreateCity import CityCreateView
from ..Views.CityViews.DeleteCity import CityDeleteView
from ..Views.CityViews.GetAllCities import CitiesGetView
from ..Views.CityViews.GetOneCity import CityGetView
from ..Views.CityViews.UpdateCity import CityUpdateView


urlpatterns = [
    path('City/create/', CityCreateView.as_view(), name='Create City'),
    path('City/<int:pk>/delete/', CityDeleteView.as_view(), name='Delete City'),
    path('Cities/', CitiesGetView.as_view(), name='Cities List'),
    path('City/<int:pk>/', CityGetView.as_view(), name='City Detail'),
    path('City/<int:pk>/update/', CityUpdateView.as_view(), name='Update City'),
]

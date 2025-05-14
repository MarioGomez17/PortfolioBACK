from django.urls import path
from ..Views.EducationPlaceViews.CreateEducationPlace import EducationPlaceCreateView
from ..Views.EducationPlaceViews.DeleteEducationPlace import EducationPlaceDeleteView
from ..Views.EducationPlaceViews.GetAllEducationPlaces import EducationPlacesGetView
from ..Views.EducationPlaceViews.GetOneEducationPlace import EducationPlaceGetView
from ..Views.EducationPlaceViews.UpdateEducationPlace import EducationPlaceUpdateView


urlpatterns = [
    path('EducationPlace/create/', EducationPlaceCreateView.as_view(), name='Create Education Place'),
    path('EducationPlace/<int:pk>/delete/', EducationPlaceDeleteView.as_view(), name='Delete Education Place'),
    path('EducationPlaces/', EducationPlacesGetView.as_view(), name='EducationPlaces List'),
    path('EducationPlace/<int:pk>/', EducationPlaceGetView.as_view(), name='EducationPlace Detail'),
    path('EducationPlace/<int:pk>/update/', EducationPlaceUpdateView.as_view(), name='Update EducationPlace'),
]
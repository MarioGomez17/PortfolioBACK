from django.urls import path
from ..Views.DevelopmentAreaViews.CreateDevelopmentArea import DevelopmentAreaCreateView
from ..Views.DevelopmentAreaViews.DeleteDevelopmentArea import DevelopmentAreaDeleteView
from ..Views.DevelopmentAreaViews.GetAllDevelopmentAreas import DevelopmentAreasGetView
from ..Views.DevelopmentAreaViews.GetOneDevelopmentArea import DevelopmentAreaGetView
from ..Views.DevelopmentAreaViews.UpdateDevelopmentArea import DevelopmentAreaUpdateView


urlpatterns = [
    path('DevelopmentArea/create/', DevelopmentAreaCreateView.as_view(), name='Create Development Area'),
    path('DevelopmentArea/<int:pk>/delete/', DevelopmentAreaDeleteView.as_view(), name='Delete Development Area'),
    path('DevelopmentAreas/', DevelopmentAreasGetView.as_view(), name='Development Areas List'),
    path('DevelopmentArea/<int:pk>/', DevelopmentAreaGetView.as_view(), name='Development Area Detail'),
    path('DevelopmentArea/<int:pk>/update/', DevelopmentAreaUpdateView.as_view(), name='Update Development Area'),
]
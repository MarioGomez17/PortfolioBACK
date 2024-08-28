from django.urls import path
from ..Views.DeveloperViews.CreateDeveloper import DeveloperCreateView
from ..Views.DeveloperViews.DeleteDeveloper import DeveloperDeleteView
from ..Views.DeveloperViews.GetAllDevelopers import DevelopersGetView
from ..Views.DeveloperViews.GetOneDeveloper import DeveloperGetView
from ..Views.DeveloperViews.UpdateDeveloper import DeveloperUpdateView


urlpatterns = [
    path('Developer/create/', DeveloperCreateView.as_view(), name='Create Developer'),
    path('Developer/<int:pk>/delete/', DeveloperDeleteView.as_view(), name='Delete Developer'),
    path('Developers/', DevelopersGetView.as_view(), name='Developers List'),
    path('Developer/<int:pk>/', DeveloperGetView.as_view(), name='Developer Detail'),
    path('Developer/<int:pk>/update/', DeveloperUpdateView.as_view(), name='Update Developer'),
]
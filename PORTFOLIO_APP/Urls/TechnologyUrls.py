from django.urls import path
from ..Views.TechnologyViews.CreateTechnology import TechnologyCreateView
from ..Views.TechnologyViews.DeleteTechnology import TechnologyDeleteView
from ..Views.TechnologyViews.GetAllTechnologies import TechnologiesGetView
from ..Views.TechnologyViews.GetOneTechnology import TechnologyGetView
from ..Views.TechnologyViews.UpdateTechnology import TechnologyUpdateView


urlpatterns = [
    path('Technology/create/', TechnologyCreateView.as_view(), name='Create Technology'),
    path('Technology/<int:pk>/delete/', TechnologyDeleteView.as_view(), name='Delete Technology'),
    path('Technologies/', TechnologiesGetView.as_view(), name='Technologies List'),
    path('Technology/<int:pk>/', TechnologyGetView.as_view(), name='Technology Detail'),
    path('Technology/<int:pk>/update/', TechnologyUpdateView.as_view(), name='Update Technology'),
]
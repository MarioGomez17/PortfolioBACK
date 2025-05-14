from django.urls import path
from ..Views.ExperienceViews.CreateExperience import ExperienceCreateView
from ..Views.ExperienceViews.DeleteExperience import ExperienceDeleteView
from ..Views.ExperienceViews.GetAllExperiences import ExperiencesGetView
from ..Views.ExperienceViews.GetOneExperience import ExperienceGetView
from ..Views.ExperienceViews.UpdateExperience import ExperienceUpdateView


urlpatterns = [
    path('Experience/create/', ExperienceCreateView.as_view(), name='Create Experience'),
    path('Experience/<int:pk>/delete/', ExperienceDeleteView.as_view(), name='Delete Experience'),
    path('Experiences/', ExperiencesGetView.as_view(), name='Experiences List'),
    path('Experience/<int:pk>/', ExperienceGetView.as_view(), name='Experience Detail'),
    path('Experience/<int:pk>/update/', ExperienceUpdateView.as_view(), name='Update Experience'),
]
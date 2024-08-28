from django.urls import path
from ..Views.ProjectViews.CreateProject import ProjectCreateView
from ..Views.ProjectViews.DeleteProject import ProjectDeleteView
from ..Views.ProjectViews.GetAllProjects import ProjectsGetView
from ..Views.ProjectViews.GetOneProject import ProjectGetView
from ..Views.ProjectViews.UpdateProject import ProjectUpdateView


urlpatterns = [
    path('Project/create/', ProjectCreateView.as_view(), name='Create Project'),
    path('Project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='Delete Project'),
    path('Projects/', ProjectsGetView.as_view(), name='Projects List'),
    path('Project/<int:pk>/', ProjectGetView.as_view(), name='Project Detail'),
    path('Project/<int:pk>/update/', ProjectUpdateView.as_view(), name='Update Project'),
]
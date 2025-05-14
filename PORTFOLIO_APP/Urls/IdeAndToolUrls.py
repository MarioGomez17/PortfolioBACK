from django.urls import path
from ..Views.IdeAndToolViews.CreateIdeAndTool import IdeAndToolCreateView
from ..Views.IdeAndToolViews.DeleteIdeAndTool import IdeAndToolDeleteView
from ..Views.IdeAndToolViews.GetAllIdesAndTools import IdesAndToolsGetView
from ..Views.IdeAndToolViews.GetOneIdeAndTool import IdeAndToolGetView
from ..Views.IdeAndToolViews.UpdateIdeAndTool import IdeAndToolUpdateView


urlpatterns = [
    path('IdeAndTool/create/', IdeAndToolCreateView.as_view(), name='Create Ide And Tool'),
    path('IdeAndTool/<int:pk>/delete/', IdeAndToolDeleteView.as_view(), name='Delete Ide And Tool'),
    path('IdesAndTools/', IdesAndToolsGetView.as_view(), name='Ides And Tools List'),
    path('IdeAndTool/<int:pk>/', IdeAndToolGetView.as_view(), name='Ide And Tool Detail'),
    path('IdeAndTool/<int:pk>/update/', IdeAndToolUpdateView.as_view(), name='Update Ide And Tool'),
]
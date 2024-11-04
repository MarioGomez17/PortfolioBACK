from django.urls import path
from ..Views.DivisionViews.CreateDivision import DivisionCreateView
from ..Views.DivisionViews.DeleteDivision import DivisionDeleteView
from ..Views.DivisionViews.GetAllDivisions import DivisionsGetView
from ..Views.DivisionViews.GetOneDivision import DivisionGetView
from ..Views.DivisionViews.UpdateDivision import DivisionUpdateView


urlpatterns = [
    path('Division/create/', DivisionCreateView.as_view(), name='Create Division'),
    path('Division/<int:pk>/delete/', DivisionDeleteView.as_view(), name='Delete Division'),
    path('Divisions/', DivisionsGetView.as_view(), name='Divisions List'),
    path('Division/<int:pk>/', DivisionGetView.as_view(), name='Division Detail'),
    path('Division/<int:pk>/update/', DivisionUpdateView.as_view(), name='Update Division'),
]
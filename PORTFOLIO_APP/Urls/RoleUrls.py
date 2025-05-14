from django.urls import path
from ..Views.RoleViews.CreateRole import RoleCreateView
from ..Views.RoleViews.DeleteRole import RoleDeleteView
from ..Views.RoleViews.GetAllRole import RolesGetView
from ..Views.RoleViews.GetOneRole import RoleGetView
from ..Views.RoleViews.UpdateRole import RoleUpdateView


urlpatterns = [
    path('Role/create/', RoleCreateView.as_view(), name='Create Role'),
    path('Role/<int:pk>/delete/', RoleDeleteView.as_view(), name='Delete Role'),
    path('Roles/', RolesGetView.as_view(), name='Roles List'),
    path('Role/<int:pk>/', RoleGetView.as_view(), name='Role Detail'),
    path('Role/<int:pk>/update/', RoleUpdateView.as_view(), name='Update Role'),
]
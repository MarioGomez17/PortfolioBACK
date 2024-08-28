from django.urls import path
from ..Views.DepartmentViews.CreateDepartment import DepartmentCreateView
from ..Views.DepartmentViews.DeleteDepartment import DepartmentDeleteView
from ..Views.DepartmentViews.GetAllDepartments import DepartmentsGetView
from ..Views.DepartmentViews.GetOneDepartment import DepartmentGetView
from ..Views.DepartmentViews.UpdateDepartment import DepartmentUpdateView


urlpatterns = [
    path('Department/create/', DepartmentCreateView.as_view(), name='Create Department'),
    path('Department/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='Delete Department'),
    path('Departments/', DepartmentsGetView.as_view(), name='Departments List'),
    path('Department/<int:pk>/', DepartmentGetView.as_view(), name='Department Detail'),
    path('Department/<int:pk>/update/', DepartmentUpdateView.as_view(), name='Update Department'),
]
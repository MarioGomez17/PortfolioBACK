from django.urls import path
from ..Views.EducationTypeViews.CreateEducationType import EducationTypeCreateView
from ..Views.EducationTypeViews.DeleteEducationType import EducationTypeDeleteView
from ..Views.EducationTypeViews.GetAllEducationTypes import EducationTypesGetView
from ..Views.EducationTypeViews.GetOneEducationType import EducationTypeGetView
from ..Views.EducationTypeViews.UpdateEducationType import EducationTypeUpdateView


urlpatterns = [
    path('EducationType/create/', EducationTypeCreateView.as_view(), name='Create EducationType'),
    path('EducationType/<int:pk>/delete/', EducationTypeDeleteView.as_view(), name='Delete EducationType'),
    path('EducationTypes/', EducationTypesGetView.as_view(), name='EducationTypes List'),
    path('EducationType/<int:pk>/', EducationTypeGetView.as_view(), name='EducationType Detail'),
    path('EducationType/<int:pk>/update/', EducationTypeUpdateView.as_view(), name='Update EducationType'),
]
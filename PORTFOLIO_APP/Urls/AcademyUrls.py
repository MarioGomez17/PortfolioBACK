from django.urls import path
from ..Views.AcademyViews.CreateAcademy import AcademyCreateView
from ..Views.AcademyViews.DeleteAcademy import AcademyDeleteView
from ..Views.AcademyViews.GetAllAcademies import AcademiesGetView
from ..Views.AcademyViews.GetOneAcademy import AcademyGetView
from ..Views.AcademyViews.UpdateAcademy import AcademyUpdateView


urlpatterns = [
    path('Academy/create/', AcademyCreateView.as_view(), name='Create Academy'),
    path('Academy/<int:pk>/delete/', AcademyDeleteView.as_view(), name='Delete Academy'),
    path('Academies/', AcademiesGetView.as_view(), name='Academies List'),
    path('Academy/<int:pk>/', AcademyGetView.as_view(), name='Academy Detail'),
    path('Academy/<int:pk>/update/', AcademyUpdateView.as_view(), name='Update Academy'),
]
from django.urls import path
from ..Views.EducationViews.CreateEducation import EducationCreateView
from ..Views.EducationViews.DeleteEducation import EducationDeleteView
from ..Views.EducationViews.GetAllEducations import EducationsGetView
from ..Views.EducationViews.GetOneEducation import EducationGetView
from ..Views.EducationViews.UpdateEducation import EducationUpdateView


urlpatterns = [
    path('Education/create/', EducationCreateView.as_view(), name='Create Education'),
    path('Education/<int:pk>/delete/', EducationDeleteView.as_view(), name='Delete Education'),
    path('Educations/', EducationsGetView.as_view(), name='Educations List'),
    path('Education/<int:pk>/', EducationGetView.as_view(), name='Education Detail'),
    path('Education/<int:pk>/update/', EducationUpdateView.as_view(), name='Update Education'),
]
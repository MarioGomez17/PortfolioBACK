from django.urls import path
from ..Views.ProgrammingLanguageViews.CreateProgrammingLanguage import ProgrammingLanguageCreateView
from ..Views.ProgrammingLanguageViews.DeleteProgrammingLanguage import ProgrammingLanguageDeleteView
from ..Views.ProgrammingLanguageViews.GetAllProgrammingLanguages import ProgrammingLanguagesGetView
from ..Views.ProgrammingLanguageViews.GetOneProgrammingLanguage import ProgrammingLanguageGetView
from ..Views.ProgrammingLanguageViews.UpdateProgrammingLanguage import ProgrammingLanguageUpdateView


urlpatterns = [
    path('ProgrammingLanguage/create/', ProgrammingLanguageCreateView.as_view(), name='Create ProgrammingLanguage'),
    path('ProgrammingLanguage/<int:pk>/delete/', ProgrammingLanguageDeleteView.as_view(), name='Delete ProgrammingLanguage'),
    path('ProgrammingLanguages/', ProgrammingLanguagesGetView.as_view(), name='ProgrammingLanguages List'),
    path('ProgrammingLanguage/<int:pk>/', ProgrammingLanguageGetView.as_view(), name='ProgrammingLanguage Detail'),
    path('ProgrammingLanguage/<int:pk>/update/', ProgrammingLanguageUpdateView.as_view(), name='Update ProgrammingLanguage'),
]
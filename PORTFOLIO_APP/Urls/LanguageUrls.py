from django.urls import path
from ..Views.LanguageViews.CreateLanguage import LanguageCreateView
from ..Views.LanguageViews.DeleteLanguage import LanguageDeleteView
from ..Views.LanguageViews.GetAllLanguages import LanguagesGetView
from ..Views.LanguageViews.GetOneLanguage import LanguageGetView
from ..Views.LanguageViews.UpdateLanguage import LanguageUpdateView


urlpatterns = [
    path('Language/create/', LanguageCreateView.as_view(), name='Create Language'),
    path('Language/<int:pk>/delete/', LanguageDeleteView.as_view(), name='Delete Language'),
    path('Languages/', LanguagesGetView.as_view(), name='Languages List'),
    path('Language/<int:pk>/', LanguageGetView.as_view(), name='Language Detail'),
    path('Language/<int:pk>/update/', LanguageUpdateView.as_view(), name='Update Language'),
]
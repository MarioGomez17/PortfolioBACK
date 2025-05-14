from django.urls import path
from ..Views.EducationAchievementViews.CreateEducationAchievement import EducationAchievementCreateView
from ..Views.EducationAchievementViews.DeleteEducationAchievement import EducationAchievementDeleteView
from ..Views.EducationAchievementViews.GetAllEducationAchievement import EducationAchievementsGetView
from ..Views.EducationAchievementViews.GetOneEducationAchievement import EducationAchievementGetView
from ..Views.EducationAchievementViews.UpdateEducationAchievement import EducationAchievementUpdateView


urlpatterns = [
    path('EducationAchievement/create/', EducationAchievementCreateView.as_view(), name='Create Educatio nAchievement'),
    path('EducationAchievement/<int:pk>/delete/', EducationAchievementDeleteView.as_view(), name='Delete Education Achievement'),
    path('EducationAchievements/', EducationAchievementsGetView.as_view(), name='Education Achievements List'),
    path('EducationAchievement/<int:pk>/', EducationAchievementGetView.as_view(), name='Education Achievement Detail'),
    path('EducationAchievement/<int:pk>/update/', EducationAchievementUpdateView.as_view(), name='Update Education Achievement'),
]
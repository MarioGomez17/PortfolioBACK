from django.urls import path
from ..Views.AchievementViews.CreateAchievement import AchievementCreateView
from ..Views.AchievementViews.DeleteAchievement import AchievementDeleteView
from ..Views.AchievementViews.GetAllAchievements import AchievementsGetView
from ..Views.AchievementViews.GetOneAchievement import AchievementGetView
from ..Views.AchievementViews.UpdateAchievement import AchievementUpdateView


urlpatterns = [
    path('Achievement/create/', AchievementCreateView.as_view(), name='Create Achievement'),
    path('Achievement/<int:pk>/delete/', AchievementDeleteView.as_view(), name='Delete Achievement'),
    path('Achievements/', AchievementsGetView.as_view(), name='Achievements List'),
    path('Achievement/<int:pk>/', AchievementGetView.as_view(), name='Achievement Detail'),
    path('Achievement/<int:pk>/update/', AchievementUpdateView.as_view(), name='Update Achievement'),
]
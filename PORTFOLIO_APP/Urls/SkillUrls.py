from django.urls import path
from ..Views.SkillViews.CreateSkill import SkillCreateView
from ..Views.SkillViews.DeleteSkill import SkillDeleteView
from ..Views.SkillViews.GetAllSkills import SkillsGetView
from ..Views.SkillViews.GetOneSkill import SkillGetView
from ..Views.SkillViews.UpdateSkill import SkillUpdateView


urlpatterns = [
    path('Skill/create/', SkillCreateView.as_view(), name='Create Skill'),
    path('Skill/<int:pk>/delete/', SkillDeleteView.as_view(), name='Delete Skill'),
    path('Skills/', SkillsGetView.as_view(), name='Skills List'),
    path('Skill/<int:pk>/', SkillGetView.as_view(), name='Skill Detail'),
    path('Skill/<int:pk>/update/', SkillUpdateView.as_view(), name='Update Skill'),
]
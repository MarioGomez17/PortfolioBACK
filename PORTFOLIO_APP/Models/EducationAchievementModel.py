from django.db import models
from .EducationModel import EducationModel

class EducationAchievementModel(models.Model):
    Id_EducationAchievement = models.AutoField(primary_key=True, db_column='Id_EducationAchievement', null=False)
    Description_EducationAchievement = models.CharField(max_length=50, db_column='Description_EducationAchievement', default='', null=False)
    Education_EducationAchievement = models.ForeignKey(EducationModel, on_delete=models.PROTECT, db_column='Education_EducationAchievement', related_name='Achievements_Education')

    def __str__(self):
        return self.Description_EducationAchievement

    class Meta:
        managed = True
        db_table = 'EducationAchievement'
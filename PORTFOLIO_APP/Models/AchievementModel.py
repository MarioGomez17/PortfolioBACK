from django.db import models
from .ExperienceModel import ExperienceModel

class AchievementModel(models.Model):
    Id_Achievement = models.AutoField(primary_key=True, db_column='Id_Achievement', null=False)
    Description_Achievement = models.TextField(db_column='Description_Achievement', default='', null=False)
    Experience_Achievement = models.ForeignKey(ExperienceModel, on_delete=models.PROTECT, db_column='Experience_Achievement', related_name='Experience_Achievements')

    def __str__(self):
        return self.Description_Achievement

    class Meta:
        managed = True
        db_table = 'Achievement'
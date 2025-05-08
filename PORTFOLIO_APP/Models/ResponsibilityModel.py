from django.db import models
from .ExperienceModel import ExperienceModel

class ResponsibilityModel(models.Model):
    Id_Responsibility = models.AutoField(primary_key=True, db_column='Id_Responsibility', null=False)
    Description_Responsibility = models.TextField(db_column='Description_Responsibility', default='', null=False)
    Experience_Responsibility = models.ForeignKey(ExperienceModel, on_delete=models.PROTECT, db_column='Experience_Responsibility', related_name='Experience_Responsibilities')

    def __str__(self):
        return self.Description_Responsibility

    class Meta:
        managed = True
        db_table = 'Responsibility'
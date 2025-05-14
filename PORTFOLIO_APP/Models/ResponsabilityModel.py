from django.db import models
from .ExperienceModel import ExperienceModel

class ResponsabilityModel(models.Model):
    Id_Responsability = models.AutoField(primary_key=True, db_column='Id_Responsability', null=False)
    Description_Responsability = models.TextField(db_column='Description_Responsability', default='', null=False)
    Experience_Responsability = models.ForeignKey(ExperienceModel, on_delete=models.PROTECT, db_column='Experience_Responsability', related_name='Experience_Responsibilities')

    def __str__(self):
        return self.Description_Responsability

    class Meta:
        managed = True
        db_table = 'Responsability'
from django.db import models
from datetime import date
from .CompanyModel import CompanyModel
from .DeveloperModel import DeveloperModel
from .RoleModel import RoleModel


class ExperienceModel(models.Model):
    Id_Experience = models.AutoField(primary_key=True, db_column='Id_Experience', null=False)
    Description_Experience = models.TextField(db_column='Description_Experience', default='', null=False)
    DateStart_Experience = models.DateField(db_column='DateStart_Experience', default=date.today, null=False)
    DateEnd_Experience = models.DateField(db_column='DateEnd_Experience', default=date.today, null=False)
    Role_Experience = models.ForeignKey(RoleModel, on_delete=models.PROTECT, db_column='Role_Experience')
    Company_Experience = models.ForeignKey(CompanyModel, on_delete=models.PROTECT, db_column='Company_Experience')
    Developer_Experience = models.ForeignKey(DeveloperModel, on_delete=models.PROTECT, db_column='Developer_Experience', related_name='Experience_Developer')

    def __str__(self):
        return self.Description_Experience

    class Meta:
        managed = True
        db_table = 'Experience'
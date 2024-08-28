from django.db import models
from .CountryModel import CountryModel


class DepartmentModel(models.Model):
    Id_Department = models.AutoField(primary_key=True, db_column='Id_Department', null=False)
    Name_Department = models.CharField(max_length=50, db_column='Name_Department', default='', null=False)
    Country_Department = models.ForeignKey(CountryModel, on_delete=models.PROTECT, db_column='Country_Department')

    def __str__(self):
        return self.Name_Department

    class Meta:
        managed = True
        db_table = 'Department'

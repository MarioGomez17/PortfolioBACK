from django.db import models
from .DepartmentModel import DepartmentModel

class CityModel(models.Model):
    Id_City = models.AutoField(primary_key=True, db_column='Id_City', null=False)
    Name_City = models.CharField(max_length=50, db_column='Name_City', default='', null=False)
    UrlMaps_City = models.Textfield(db_column='UrlMaps_City', default='', null=False)
    Department_City = models.ForeignKey(DepartmentModel, on_delete=models.PROTECT, db_column='Department_City')

    def __str__(self):
        return self.Name_City

    class Meta:
        managed = True
        db_table = 'City'

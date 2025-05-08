from django.db import models
from .CityModel import CityModel


class CompanyModel(models.Model):
    Id_Company = models.AutoField(primary_key=True, db_column='Id_Company', null=False)
    Name_Company = models.CharField(max_length=150, db_column='Name_Company', default='', null=False)
    Boss_Company = models.CharField(max_length=100, db_column='Boss_Company', default='', null=False)
    City_Company = models.ForeignKey(CityModel, on_delete=models.PROTECT, db_column='City_Company')

    def __str__(self):
        return self.Name_Company

    class Meta:
        managed = True
        db_table = 'Company'

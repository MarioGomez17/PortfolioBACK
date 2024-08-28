from django.db import models


class CountryModel(models.Model):
    Id_Country = models.AutoField(primary_key=True, db_column='Id_Country', null=False)
    Name_Country = models.CharField(max_length=50, db_column='Name_Country', default='', null=False)

    def __str__(self):
        return self.Name_Country

    class Meta:
        managed = True
        db_table = 'Country'

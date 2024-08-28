from django.db import models


class DivisionModel(models.Model):
    Id_Division = models.AutoField(primary_key=True, db_column='Id_Division', null=False)
    Name_Division = models.CharField(max_length=50, db_column='Name_Division', default='', null=False)

    def __str__(self):
        return self.Name_Division

    class Meta:
        managed = True
        db_table = 'Division'

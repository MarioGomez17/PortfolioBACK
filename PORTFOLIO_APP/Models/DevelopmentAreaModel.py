from django.db import models


class DevelopmentAreaModel(models.Model):
    Id_DevelopmentArea = models.AutoField(primary_key=True, db_column='Id_DevelopmentArea', null=False)
    Name_DevelopmentArea = models.CharField(max_length=50, db_column='Name_DevelopmentArea', default='', null=False)

    def __str__(self):
        return self.Name_DevelopmentArea

    class Meta:
        managed = True
        db_table = 'DevelopmentArea'
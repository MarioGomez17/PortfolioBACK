from django.db import models


class ControlVersionModel(models.Model):
    Id_ControlVersion = models.AutoField(primary_key=True, db_column='Id_ControlVersion', null=False)
    Name_ControlVersion = models.CharField(max_length=50, db_column='Name_ControlVersion', default='', null=False)

    def __str__(self):
        return self.Name_ControlVersion

    class Meta:
        managed = True
        db_table = 'ControlVersion'
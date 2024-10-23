from django.db import models

class AcademyModel(models.Model):
    Id_Academy = models.AutoField(primary_key=True, db_column='Id_Academy', null=False)
    Name_Academy = models.CharField(max_length=50, db_column='Name_Academy', default='', null=False)

    def __str__(self):
        return self.Name_Academy

    class Meta:
        managed = True
        db_table = 'Academy'
from django.db import models

class EducationTypeModel(models.Model):
    Id_EducationType = models.AutoField(primary_key=True, db_column='Id_EducationType', null=False)
    Name_EducationType = models.CharField(max_length=50, db_column='Name_EducationType', default='', null=False)

    def __str__(self):
        return self.Name_EducationType

    class Meta:
        managed = True
        db_table = 'EducationType'
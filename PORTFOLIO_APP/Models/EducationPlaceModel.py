from django.db import models

class EducationPlaceModel(models.Model):
    Id_EducationPlace = models.AutoField(primary_key=True, db_column='Id_EducationPlace', null=False)
    Name_EducationPlace = models.CharField(max_length=50, db_column='Name_EducationPlace', default='', null=False)

    def __str__(self):
        return self.Name_EducationPlace

    class Meta:
        managed = True
        db_table = 'EducationPlace'
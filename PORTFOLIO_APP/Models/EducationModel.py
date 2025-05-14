from django.db import models
from .AcademyModel import AcademyModel
from .EducationTypeModel import EducationTypeModel
from .EducationPlaceModel import EducationPlaceModel
from .DeveloperModel import DeveloperModel

class EducationModel(models.Model):
    Id_Education = models.AutoField(primary_key=True, db_column='Id_Education', null=False)
    DegreeName_Education = models.CharField(max_length=300, db_column='DegreeName_Education', default='', null=False)
    Description_Education = models.CharField(max_length=300, db_column='Description_Education', default='', null=False)
    Date_Education = models.CharField(max_length=300, db_column='Date_Education', default='', null=False)
    DegreeFile_Education = models.CharField(max_length=300, db_column='DegreeFile_Education', default='', null=False)
    Academy_Education = models.ForeignKey(AcademyModel, on_delete=models.PROTECT, db_column='Academy_Education')
    EducationType_Education = models.ForeignKey(EducationTypeModel, on_delete=models.PROTECT, db_column='EducationType_Education')
    EducationPlace_Education = models.ForeignKey(EducationPlaceModel, on_delete=models.PROTECT, db_column='EducationPlace_Education')
    Developer_Education = models.ForeignKey(DeveloperModel, on_delete=models.PROTECT, db_column='Developer_Education', related_name='Education_Developer')

    def __str__(self):
        return self.Name_Education

    class Meta:
        managed = True
        db_table = 'Education'
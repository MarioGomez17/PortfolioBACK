from django.db import models
from .AcademyModel import AcademyModel
from .EducationTypeModel import EducationTypeModel
from .DeveloperModel import DeveloperModel

class EducationModel(models.Model):
    Id_Education = models.AutoField(primary_key=True, db_column='Id_Education', null=False)
    DegreeName_Education = models.CharField(max_length=300, db_column='DegreeName_Education', default='', null=False)
    DegreeFile_Education = models.CharField(max_length=300, db_column='DegreeFile_Education', default='', null=False)
    Academy_Education = models.ForeignKey(AcademyModel, on_delete=models.PROTECT, db_column='Academy_Education')
    Developer_Education = models.ForeignKey(DeveloperModel, on_delete=models.PROTECT, db_column='Developer_Education', related_name='Education_Developer')
    EducationType_Education = models.ForeignKey(EducationTypeModel, on_delete=models.PROTECT, db_column='EducationType_Education')

    def __str__(self):
        return self.Name_Education

    class Meta:
        managed = True
        db_table = 'Education'
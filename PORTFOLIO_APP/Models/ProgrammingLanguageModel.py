from django.db import models
from .DevelopmentAreaModel import DevelopmentAreaModel

class ProgrammingLanguageModel(models.Model):
    Id_ProgrammingLanguage = models.AutoField(primary_key=True, db_column='Id_ProgrammingLanguage', null=False)
    Name_ProgrammingLanguage = models.CharField(max_length=50, db_column='Name_ProgrammingLanguage', default='', null=False)
    Description_ProgrammingLanguage = models.CharField(max_length=1000, db_column='Description_ProgrammingLanguage', default='', null=False)
    Logo_ProgrammingLanguage = models.TextField(db_column='Logo_ProgrammingLanguage', default='', null=False)
    DevelopmentArea_ProgrammingLanguage = models.ForeignKey(DevelopmentAreaModel, on_delete=models.PROTECT, db_column='DevelopmentArea_ProgrammingLanguage', default=1, null=True)

    def __str__(self):
        return self.Name_ProgrammingLanguage

    class Meta:
        managed = True
        db_table = 'ProgrammingLanguage'
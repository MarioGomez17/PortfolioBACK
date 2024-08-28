from django.db import models


class ProgrammingLanguageModel(models.Model):
    Id_ProgrammingLanguage = models.AutoField(primary_key=True, db_column='Id_ProgrammingLanguage', null=False)
    Name_ProgrammingLanguage = models.CharField(max_length=50, db_column='Name_ProgrammingLanguage', default='', null=False)

    def __str__(self):
        return self.Name_ProgrammingLanguage

    class Meta:
        managed = True
        db_table = 'ProgrammingLanguage'

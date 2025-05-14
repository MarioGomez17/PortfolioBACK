from django.db import models


class LanguageModel(models.Model):
    Id_Language = models.AutoField(primary_key=True, db_column='Id_Language', null=False)
    Name_Language = models.CharField(max_length=50, db_column='Name_Language', default='', null=False)
    Level_Language = models.CharField(max_length=50, db_column='Level_Language', default='', null=False)

    def __str__(self):
        return self.Name_Language

    class Meta:
        managed = True
        db_table = 'Language'
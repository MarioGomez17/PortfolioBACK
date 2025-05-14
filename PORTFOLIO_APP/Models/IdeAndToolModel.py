from django.db import models


class IdeAndToolModel(models.Model):
    Id_IdeAndTool = models.AutoField(primary_key=True, db_column='Id_IdeAndTool', null=False)
    Name_IdeAndTool = models.CharField(max_length=50, db_column='Name_IdeAndTool', default='', null=False)

    def __str__(self):
        return self.Name_IdeAndTool

    class Meta:
        managed = True
        db_table = 'IdeAndTool'
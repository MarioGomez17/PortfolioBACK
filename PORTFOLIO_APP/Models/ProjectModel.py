from django.db import models


class ProjectModel(models.Model):
    Id_Project = models.AutoField(primary_key=True, db_column='Id_Project', null=False)
    Name_Project = models.CharField(max_length=50, db_column='Name_Project', default='', null=False)
    URL_Project = models.URLField(db_column='URL_Project', default='', null=False)
    Technologies_Project = models.ManyToManyField('TechnologyModel')

    def __str__(self):
        return self.Name_Project

    class Meta:
        managed = True
        db_table = 'Project'

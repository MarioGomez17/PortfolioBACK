from django.db import models
from .DeveloperModel import DeveloperModel

class ProjectModel(models.Model):
    Id_Project = models.AutoField(primary_key=True, db_column='Id_Project', null=False)
    Name_Project = models.CharField(max_length=50, db_column='Name_Project', default='', null=False)
    Description_Project = models.TextField(db_column='Description_Project', default='', null=False)
    URL_Project = models.URLField(db_column='URL_Project', default='', null=False)
    GitHubUrl_Project = models.URLField(db_column='GitHubUrl_Project', default='', null=False)
    Image_Project = models.URLField(db_column='Image_Project', default='', null=False)
    IsFeatured_Project = models.URLField(db_column='IsFeatured_Project', default='', null=False)
    Technologies_Project = models.ManyToManyField('TechnologyModel')
    Developer_Project = models.ForeignKey(DeveloperModel, on_delete=models.PROTECT, db_column='Developer_Project', related_name='Projects_Developer')

    def __str__(self):
        return self.Name_Project

    class Meta:
        managed = True
        db_table = 'Project'

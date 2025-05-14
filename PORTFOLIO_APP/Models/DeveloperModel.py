from django.db import models
from .CityModel import CityModel

class DeveloperModel(models.Model):
    Id_Developer = models.AutoField(primary_key=True, db_column='Id_Developer', null=False)
    Name_Developer = models.CharField(max_length=50, db_column='Name_Developer', default='', null=False)
    LastName_Developer = models.CharField(max_length=50, db_column='LastName_Developer', default='', null=False)
    Email_Developer = models.EmailField(db_column='Email_Developer', default='', null=False)
    Phone_Developer = models.CharField(max_length=15, db_column='Phone_Developer', default='', null=False)
    LinkedinName_Developer = models.URLField(db_column='LinkedinName_Developer', default='', null=False)
    LinkedinUrl_Developer = models.URLField(db_column='LinkedinUrl_Developer', default='', null=False)
    GitHubName_Developer = models.URLField(db_column='GitHubName_Developer', default='', null=False)
    GitHubUrl_Developer = models.URLField(db_column='GitHubUrl_Developer', default='', null=False)
    Role_Developer = models.URLField(db_column='Role_Developer', default='', null=False)
    ShortProfile_Developer = models.TextField(db_column='ShortProfile_Developer', default='', null=False)
    LongProfile_Developer = models.TextField(db_column='LongProfile_Developer', default='', null=False)
    City_Developer = models.ForeignKey(CityModel, on_delete=models.PROTECT, db_column='City_Developer')
    ProgrammingLanguages_Developer = models.ManyToManyField('ProgrammingLanguageModel')
    Technologies_Developer = models.ManyToManyField('TechnologyModel')
    IdesAndTools_Developer = models.ManyToManyField('IdeAndToolModel')
    ControlsVersionDeveloper = models.ManyToManyField('ControlVersionModel')
    Skills_Developer = models.ManyToManyField('SkillModel')
    Languages_Developer = models.ManyToManyField('LanguageModel')

    def __str__(self):
        return self.Name_Developer

    class Meta:
        managed = True
        db_table = 'Developer'

from django.db import models
from .SkillModel import SkillModel

class TechnologyModel(models.Model):
    Id_Technology = models.AutoField(primary_key=True, db_column='Id_Technology', null=False)
    Name_Technology = models.CharField(max_length=50, db_column='Name_Technology', default='', null=False)
    Logo_Technology = models.TextField(db_column='Logo_Technology', default='', null=False)
    Skill_Technology = models.ForeignKey(SkillModel, on_delete=models.PROTECT, db_column='Skill_Technology', default=1)


    def __str__(self):
        return self.Name_Technology

    class Meta:
        managed = True
        db_table = 'Technology'

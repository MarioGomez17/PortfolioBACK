from django.db import models


class SkillModel(models.Model):
    Id_Skill = models.AutoField(primary_key=True, db_column='Id_Skill', null=False)
    Name_Skill = models.CharField(max_length=50, db_column='Name_Skill', default='', null=False)

    def __str__(self):
        return self.Name_Skill

    class Meta:
        managed = True
        db_table = 'Skill'
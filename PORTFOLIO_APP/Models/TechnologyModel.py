from django.db import models
from .DivisionModel import DivisionModel

class TechnologyModel(models.Model):
    Id_Technology = models.AutoField(primary_key=True, db_column='Id_Technology', null=False)
    Name_Technology = models.CharField(max_length=50, db_column='Name_Technology', default='', null=False)
    Division_Technology = models.ForeignKey(DivisionModel, on_delete=models.PROTECT, db_column='Division_Technology')
    Logo_Technology = models.TextField(db_column='Logo_Technology', default='', null=False)


    def __str__(self):
        return self.Name_Technology

    class Meta:
        managed = True
        db_table = 'Technology'

from django.db import models


class RoleModel(models.Model):
    Id_Role = models.AutoField(primary_key=True, db_column='Id_Role', null=False)
    Name_Role = models.CharField(max_length=50, db_column='Name_Role', default='', null=False)

    def __str__(self):
        return self.Name_Role

    class Meta:
        managed = True
        db_table = 'Role'
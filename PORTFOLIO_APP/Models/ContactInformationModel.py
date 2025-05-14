from django.db import models
from .DeveloperModel import DeveloperModel

class ContactInformationModel(models.Model):
    Id_ContactInformation = models.AutoField(primary_key=True, db_column='Id_ContactInformation', null=False)
    PersonName_ContactInformation = models.CharField(max_length=150, db_column='PersonName_ContactInformation', default='', null=False)
    PersonEmail_ContactInformation = models.CharField(max_length=150, db_column='PersonEmail_ContactInformation', default='', null=False)
    PersonPhone_ContactInformation = models.CharField(max_length=150, db_column='PersonPhone_ContactInformation', default='', null=False)
    Subject_ContactInformation = models.CharField(max_length=150, db_column='Subject_ContactInformation', default='', null=False)
    BudgetRange_ContactInformation = models.CharField(max_length=150, db_column='BudgetRange_ContactInformation', default='', null=False)
    Message_ContactInformation = models.CharField(max_length=100, db_column='Message_ContactInformation', default='', null=False)
    ContactMethod_ContactInformation = models.CharField(max_length=100, db_column='ContactMethod_ContactInformation', default='', null=False)
    Developer_ContactInformation = models.ForeignKey(DeveloperModel, on_delete=models.PROTECT, db_column='ContactInformation_Developer', related_name='ContactsInformation_Developer')

    def __str__(self):
        return self.Subject_ContactInformation

    class Meta:
        managed = True
        db_table = 'ContactInformation'
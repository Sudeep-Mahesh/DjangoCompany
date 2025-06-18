from django.db import models

# Create your models here.

class Company(models.Model):
    CompanyID = models.IntegerField(primary_key=True, auto_created=True)
    CompanyName = models.CharField(max_length=25)


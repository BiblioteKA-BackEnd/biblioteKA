from pyexpat import model
from django.db import models

# Create your models here.

class Lending(models.Model):
    copy_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    devolution_at = models.DateTimeField(null=True)
    ...

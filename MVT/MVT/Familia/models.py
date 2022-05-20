from django.db import models

class familiares(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()
    documento = models.IntegerField()

from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
class Mensaje(models.Model):
    fecha = models.DateField(default=date.today)
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    mensaje = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.nombre} {self.email}"
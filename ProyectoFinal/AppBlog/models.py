from django.db import models

# Create your models here.
class Mensaje(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    mensaje = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{self.nombre} {self.email}"
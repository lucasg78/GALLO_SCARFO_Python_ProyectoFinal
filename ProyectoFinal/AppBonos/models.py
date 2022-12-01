from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cantante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Album(models.Model):
    nombre = models.CharField(max_length=30)
    cant_temas = models.IntegerField()
    fecha_de_lanzamiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}"


class Concierto(models.Model):
    nombre = models.CharField(max_length=30)
    lugar = models.CharField(max_length=30)
    fecha_de_concierto = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}"


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}"


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Guardar avatares en la carpeta media/avatares
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

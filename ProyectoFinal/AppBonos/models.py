from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dolar(models.Model):
    codigo = models.CharField(max_length=30)
    denominacion = models.CharField(max_length=100)
    emisor = models.CharField(max_length=30)
    fecha_emision = models.DateField(null=True)
    fecha_vencimiento = models.DateField(null=True)
    amortizacion = models.CharField(max_length=500)
    interes = models.CharField(max_length=500)
    ley = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.codigo} {self.denominacion}"


class Peso(models.Model):
    codigo = models.CharField(max_length=30)
    denominacion = models.CharField(max_length=100)
    emisor = models.CharField(max_length=30)
    fecha_emision = models.DateField(null=True)
    fecha_vencimiento = models.DateField(null=True)
    amortizacion = models.CharField(max_length=500)
    interes = models.CharField(max_length=500)
    ley = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.codigo} {self.denominacion}"


class Pesobd(models.Model):
    codigo = models.CharField(max_length=30)
    denominacion = models.CharField(max_length=100)
    emisor = models.CharField(max_length=30)
    fecha_emision = models.DateField(null=True)
    fecha_vencimiento = models.DateField(null=True)
    amortizacion = models.CharField(max_length=500)
    interes = models.CharField(max_length=500)
    ley = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.codigo} {self.denominacion}"


class Pesodl(models.Model):
    codigo = models.CharField(max_length=30)
    denominacion = models.CharField(max_length=100)
    emisor = models.CharField(max_length=30)
    fecha_emision = models.DateField(null=True)
    fecha_vencimiento = models.DateField(null=True)
    amortizacion = models.CharField(max_length=500)
    interes = models.CharField(max_length=500)
    ley = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.codigo} {self.denominacion}"


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Guardar avatares en la carpeta media/avatares
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

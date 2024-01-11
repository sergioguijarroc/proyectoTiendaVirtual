from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    vip = models.BooleanField(default=False)
    saldo = models.FloatField(default=0)

    def __str__(self):
        return self.username


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)]
    )
    modelo = models.CharField(max_length=50)
    vip = models.BooleanField(default=False)
    unidades_stock = models.IntegerField(default=0)
    marca = models.ForeignKey("Marca", on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    class Meta:
        unique_together = ("modelo", "marca")
        verbose_name_plural = "Productos"


class Marca(models.Model):
    nombre = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, unique=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    unidades = models.IntegerField(default=0)
    iva = models.FloatField(default=1.21)
    importe = models.FloatField(default=0)

    def __str__(self):
        return self.usuario.nombre + " - " + str(self.fecha)

    def calcularImporte(self):
        self.importe = self.producto.precio * self.unidades * self.iva

    class Meta:
        unique_together = ("fecha", "usuario", "producto")
        verbose_name_plural = "Compras"

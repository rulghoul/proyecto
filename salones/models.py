from django.db import models

# Create your models here.
class TipoSalon(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nombre


class Imagen(models.Model):
    nombre = models.ImageField(upload_to ='uploads/%Y/%m/%d/')
    def __str__(self) -> str:
        return self.nombre.name

class Servicio(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nombre

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    codigo_postal = models.CharField(max_length=5)
    colonia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Calle: {self.calle} CP: {self.codigo_postal}"

class Salon(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoSalon, on_delete=models.DO_NOTHING)
    servicios = models.ManyToManyField(Servicio)
    imagenes = models.ManyToManyField(Imagen)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre

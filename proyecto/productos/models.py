from django.db import models

# Create your models here.

class Productos(models.Model):

    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"

    nombre = models.CharField("nombre", max_length=300, default="Sin nombrar")
    descripcion = models.CharField("descripcion", max_length=300, default="Sin especificar")
    precio = models.IntegerField("precio",  default=0)
    fecha_registro = models.IntegerField("fecha_registro",  default=2023)
    estatus = models.BooleanField("estatus",  blank=False)
    
    def _str_(self):
        return self.nombre
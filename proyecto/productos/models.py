from django.db import models

# Create your models here.

class Productos(models.Model):

    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"

    nombre = models.CharField("nombre", max_length=300, default="Sin nombrar")
    descripcion = models.CharField("descripcion", max_length=300, default="Sin especificar")
    precio = models.DecimalField("precio",  default=0,max_digits=6, decimal_places=2)
    fecha_registro = models.DateField("fecha_registro", auto_now_add=False, default="YYYY-MM-DD")
    estatus = models.BooleanField("estatus",  blank=False)
    
    def _str_(self):
        return self.nombre
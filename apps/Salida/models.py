from django.db import models

# Create your models here.
class RegistrosSalidas(models.Model):
    
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fechaSalida =models.TimeField(auto_now=True)

    def __str__(self):
        return self.nombre 
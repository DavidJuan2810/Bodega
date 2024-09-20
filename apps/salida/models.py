from django.db import models

# Create your models here.


class Salida(models.Model):
    nombre = models.CharField(max_length=20)
    categoria=models.CharField(max_length=100)
    cantidad=models.IntegerField()
    FechaSalida=models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.TextField(max_length=100)
    cantidad = models.IntegerField()
    FechaIngreso=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
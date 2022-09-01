from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.


class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = "Categorias"

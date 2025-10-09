from django.db import models
from django.core.exceptions import ValidationError

class Sinis(models.Model):
    asunto = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    fecha = models.DateField()

    imagen1 = models.ImageField(upload_to='Cliente', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Cliente', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Cliente', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Cliente', null=True, blank=True)
    imagen5 = models.ImageField(upload_to='Cliente', null=True, blank=True)

    expli1 = models.CharField(max_length=100, blank=True)
    expli2 = models.CharField(max_length=100, blank=True)
    expli3 = models.CharField(max_length=100, blank=True)
    expli4 = models.CharField(max_length=100, blank=True)
    expli5 = models.CharField(max_length=100, blank=True)

def clean(self):
    pares = [
        (self.imagen1, self.expli1, '1'),
        (self.imagen2, self.expli2, '2'),
        (self.imagen3, self.expli3, '3'),
        (self.imagen4, self.expli4, '4'),
        (self.imagen5, self.expli5, '5'),
    ]

    errores = {}

    for imagen, expli, n in pares:
        if imagen and not expli:
            errores[f"expli{n}"] = f"Debe ingresar una descripción si se sube la imagen {n}."
        if expli and not imagen:
            errores[f"imagen{n}"] = f"Debe subir una imagen si escribe una descripción en expli{n}."

    if errores:
        raise ValidationError(errores)

def __str__(self):
      return self.asunto
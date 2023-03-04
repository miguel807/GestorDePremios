from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Premios(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="premios",blank=False,null=False)
    nombreObra = models.CharField(max_length=100,blank=False,null=False)
    facultad = models.CharField(max_length=100, blank=False, null=False)
    premio = models.CharField(max_length=100, blank=False, null=False)
    manifestacion = models.CharField(max_length=100, blank=False, null=False)
    existe = models.BooleanField(default=True)


    def __str__(self):
        return self.nombreObra



class Obrass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="obrass", blank=False, null=False)
    nombreObra = models.CharField(max_length=100, blank=False, null=False)
    facultad = models.CharField(max_length=100, blank=False, null=False)
    manifestacion = models.CharField(max_length=100, blank=False, null=False)
    existe = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreObra


class Cronograma(models.Model):
    fecha = models.CharField(max_length=100, blank=False, null=False)
    hora = models.CharField(max_length=100, blank=False, null=False)
    facultad = models.CharField(max_length=100, blank=False, null=False)
    lugar =  models.CharField(max_length=100, blank=False, null=False)

class Jurado(models.Model):
    nombreJurado = models.CharField(max_length=100, blank=False, null=False)
    ocupacion =  models.CharField(max_length=100, blank=False, null=False)
    manifestacionArtistica = models.CharField(max_length=100, blank=False, null=False)
from django.db import models
from django.urls import reverse
class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
class Genero(models.Model):
    nombregenero=models.CharField(max_length=100,help_text="Genero de la pelicula")

    def __str__(self):
        return self.nombregenero

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    año = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary=models.TextField(max_length=100,help_text="Sinopsis de pelicula")
    gebero_pelicula=models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reversed("pelicula-detail",args=[str(self.id)])
# Create your models here.

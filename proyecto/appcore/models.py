from django.db import models

# Create your models here.
class Pelicula(models.Model):
    tipo= models.CharField(max_length=40)
    nombre=models.CharField(max_length=100)
    duracion=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    calificacion=models.CharField(max_length=40)

    def __str__(self) -> str:
        return (f"TIPO= {self.tipo} - TITULO= {self.nombre} - DURACION= {self.duracion} - GENERO= {self.genero} - CALIFICACION= {self.calificacion}")
    
class Serie(models.Model):
    tipo= models.CharField(max_length=40)
    nombre=models.CharField(max_length=100)
    duracion=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    calificacion=models.CharField(max_length=40)

    def __str__(self) -> str:
        return (f"TIPO= {self.tipo} - TITULO= {self.nombre} - DURACION= {self.duracion} - GENERO= {self.genero} - CALIFICACION= {self.calificacion}")
    
    

class Genero(models.Model):
    genero=models.CharField(max_length=40)

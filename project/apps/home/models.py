from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    def __str__(self):
        return self.titulo
    
    
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    
class meta:
    verbose_name = "categoria"
    verbose_name_plural = "categorias"
    ordering = ['-Created']
    
def __str__(self):
    return self.name
    
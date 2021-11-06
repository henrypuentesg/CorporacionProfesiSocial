from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen",upload_to="Services")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")


class Meta:
    verbose_name = "servicio"
    verbose_name_plural = "Servicios"
    ordering = ['-created']
    
    
def __str__(self):
    return self.tittle
from django.db import models

# Create your models here.
class Project (models.Model):
    #DEFINICION DE COLUMNAS DE LA TABLA 'Project'
    title = models.CharField(max_length=250, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to = 'projects')
    link = models.URLField(null=True, blank=True, verbose_name='URL/Link del proyecto')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    #SUB-CLASE 'META' USADA PARA EXTENDER LOS 'meta datos' DE DISE;O
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']


    def __str__(self):
        return self.title
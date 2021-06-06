from django.db import models
from datetime import date
from ckeditor.fields import RichTextField

# Create your models here.
#==========================================================================================
#==========================================================================================
class Description(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name='Imagen de Perfil', upload_to = 'about')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Descripcion'
        verbose_name_plural = 'Descripcion'
        ordering = ['-created']

    def __str__(self):
        return self.name

#==========================================================================================
#==========================================================================================
class ExperiencieA(models.Model):
    # DECLARACION DE CAMPOS DE LA TABLA/ PROPIEDADES DEL MODELO
    start = models.DateField(verbose_name="Fecha de Inicio", default=date.today)
    end = models.DateField(verbose_name="Fecha de Culminación", default=date.today)
    title = models.CharField(max_length=100, verbose_name="Titulo de la experiencia")
    institute = models.CharField(max_length=100, verbose_name="Institución")
    city = models.CharField(max_length=100, verbose_name="Ciudad", )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Experiencia Academica'
        verbose_name_plural = 'Experiencias Academicas'
        ordering = ['-created']

    def __str__(self):
        return self.title

class ExperiencieL(models.Model):
    # DECLARACION DE CAMPOS DE LA TABLA/ PROPIEDADES DEL MODELO
    start = models.DateField(verbose_name="Fecha de Inicio", default=date.today)
    end = models.DateField(verbose_name="Fecha de Culminación", default=date.today)
    title = models.CharField(max_length=100, verbose_name="Titulo de la experiencia")
    institute = models.CharField(max_length=100, verbose_name="Institución")
    description = models.TextField(verbose_name="Descripcion del cargo")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencias Laborales'
        ordering = ['-created']

    def __str__(self):
        return self.title
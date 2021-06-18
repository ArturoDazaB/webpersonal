from django.db import models
from datetime import date
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField

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
class Base(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created']

    start = models.DateField(verbose_name="Fecha de Inicio", default=date.today)
    end = models.DateField(verbose_name="Fecha de Culminación", default=date.today)
    title = models.CharField(max_length=100, verbose_name="Titulo de la experiencia")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')    

class ExperiencieA(Base):
    # DECLARACION DE CAMPOS DE LA TABLA/ PROPIEDADES DEL MODELO
    institute = models.CharField(max_length=100, verbose_name="Institución")
    city = models.CharField(max_length=100, verbose_name="Ciudad")

    class Meta(Base.Meta):
        verbose_name = 'Experiencia Academica'
        verbose_name_plural = 'Experiencias Academicas'
        
        
    def __str__(self):
        return self.title

class ExperiencieL(Base):
    # DECLARACION DE CAMPOS DE LA TABLA/ PROPIEDADES DEL MODELO
    employeer = models.CharField(max_length=100, verbose_name="Ente empleador", default='')
    description = RichTextField(verbose_name="Descripcion del cargo")

    class Meta(Base.Meta):
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencias Laborales'

    def __str__(self):
        return self.title

#==========================================================================================
#==========================================================================================
# DECLARACION DE UNA CLASE BASE ABSTRACTA
# NOTA: LAS CLASES ABSTRACTAS SON UTILES CUANDO SE NECESITA AGRUPAR CAMPOS COMUNES ENTRE
# CLASES MODELOS. PARA DEFINIR UNA CLASE MODELO DEL TIPO "BASE ABSTRACTA" ES NECESARIO
# INDICAR COMO TRUE EL CAMPO "abstract" EN LA SUB-CLASE META DE LA CLASE MODELO BASE. 
class Base2(models.Model):
    #DECLARACION DE LA TUPLA 'category_choices'
    category_choices = [('skills', (
                            ('lenguajes','Lenguajes de Programacion'),
                            ('frameworks', 'Frameworks - Marcos de Trabajo'),
                            ('db', 'Bases de datos - Data bases'),
                        )),
                        ('idiomas', 'Idiomas - Lenguajes'),
                        ('aptitudes', 'Aptitudes - Habilidades personales'),
                        ('intereses', 'Intereses - Hobbies')
                        ]

    #DECLARACION DE LOS CAMPOS DE LA CLASE MODELO 'BASE'
    category = models.CharField(max_length=20, choices=category_choices ,verbose_name='Categorias')
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')


    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name    
    

class skills_idiomas (Base2):

    _choices = [(1, 'Basico (competente)'),
                (2, 'Intermedio'),
                (3, 'Avanzado')]

    knowledge_level = models.IntegerField(choices=_choices,
                                          default=_choices[0],
                                          verbose_name="Nivel de conocimiento")

    class Meta(Base2.Meta):
        abstract = False
        verbose_name = 'Habilitad Tecnica & Idioma'


class intereses_aptitudes(Base2):

    _choices = [('-', (
                    ('in', 'Interes'),
                    ('hb', 'Hobbie'),
                )),
                ('ap', 'Aptitud')]

    _subcategory = models.CharField(max_length=2, choices=_choices, verbose_name='Sub categoria', default=_choices[0])
    description = RichTextField(verbose_name='Descripcion')

    class Meta(Base2.Meta):
        abstract = False
        verbose_name = 'Intereses & Aptitudes'
#==========================================================================================
#==========================================================================================
from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    #ASIGNACION DE NOMBRE PUBLICO A LA APP 'Portfolio' (CONFIGURACION EXTENDIDA) 
    verbose_name = 'Portafolio'

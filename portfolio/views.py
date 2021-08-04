from django.shortcuts import render
from .models import Project, ProjectImages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA EL PORTAFOLIO.

class PortfolioListView(ListView):
    model = Project

class PortfolioDetailView(DetailView):
    model = Project

    # FUNCION PARA SOBRESCRIBIR EL DICCIONARIO DE CONTEXTO UTILIZADO EN LOS TEMPLATES
    def get_context_data(self, **kwargs):
        # SE LLAMA PRIMERO A LA IMPLEMENTACION BASE (super) PARA OBTENER EL DICCIONARIO DE CONTEXTO
        context = super().get_context_data(**kwargs)
        # SE RECIBE Y ALMANCENA EN LA VARIABLE LOCAL "current_project" EL OBJETO "Project" 
        # SELECCIONADO EN EL LINK "Más Información"
        current_project = super().get_object()
        # AÑADIMOS AL DICCIONARIO DE CONTEXTO UNA NUEVA TUPLA DENOMINADA "project_images" CON LAS IMAGENES DEL PROJECTO
        # SELECCIONADO EN EL LINK "Más Información" 
        context['project_images'] = ProjectImages.objects.all().filter(project = current_project)
        # RETORNAMOS LA INFORMACON DEL CONTEXTO
        return context
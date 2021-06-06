from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Description, ExperiencieA, ExperiencieL

# Create your views here.
#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION.

def about(request):
    description = Description.objects.first()
    experiencia_academica = ExperiencieA.objects.all()
    experiencia_laboral = ExperiencieL.objects.all()
    return render(request, 'about/about.html', {'descripcion':description,'eAcademica':experiencia_academica, 'eLaboral':experiencia_laboral})
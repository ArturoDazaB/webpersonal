from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Description, ExperiencieA, ExperiencieL, skills_idiomas

# Create your views here.
#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION.

def about(request):

    flag_EA = False
    flag_EL = False
    flag_L = False

    description = Description.objects.first()
    experienciaA = ExperiencieA.objects.all()
    experienciaL = ExperiencieL.objects.all()
    s_h = skills_idiomas.objects.all()
    
    if (experienciaA.count() != '0'):
        flag_EA = True

    if (experienciaL.count() != '0'):
        flag_EL = True

    if (s_h.count() != '0'):
        flag_L = True

    return render(request, 'about/about.html', {'descripcion':description,
                           'eAcademica':experienciaA,
                           'eLaboral':experienciaL,
                           'EA_Any':flag_EA,
                           'EL_Any':flag_EL,
                           'Skill_Idiomas':s_h,
                           'L_Any': flag_L,})
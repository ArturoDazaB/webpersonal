from django.shortcuts import get_list_or_404, render
from .models import Description, ExperiencieA, ExperiencieL, intereses_hobbies, intereses_hobbies_images, skills_idiomas

# Create your views here.
#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION.

def about(request):

    # CONSTANTE QUE DEFINE EL TAMAÑO DE LA FUENTE SELECCIONADA PARA PARRAFOS
    header_font_size = '22px'
    label_font_size = '17px'

    # CONSTANTE QUE DEFINE EL TAMAÑO DE LA FUENTE SELECCIONADA PARA FECHAS Y UBICACIONES 
    # (ESPECIFICAMENTE FECHAS Y UBICACIONES DE EXPERIENCIAS ACADEMICAS Y LABORALES)
    exp_font_size = '14px'

    # SE INICIALIZAN LAS BANDERAS "flag_EA" (flag/bandera experiencia academica), "flag_EL"
    # (flag/bandera experiencia laboral), "flag_L" (flag/bandera de Lenguajes) y "flag_H"
    # (flag/bandera Hobbies e Intereses)
    # ESTAS VARIABLES SE ENCARGARAN DE DETECTAR SI EXISTEN REGISTROS DE LOS MODELOS "ExperienciaA"
    # "ExperienciaL" Y "skill_idiomas" (habilidades_idiomas) DENTRO DE LA BASE DE DATOS
    flag_EA = False
    flag_EL = False
    flag_L = False
    flag_HI = False

    # OBTENEMOS TODOS LOS REGISTROS DE LOS MODELOS "Description", "ExperienciaA", "ExperienciaL"
    # Y "skill_idiomas".
    # NOTA: A DIFERENCIA DE LA BUSQUEDA DE TODOS LOS OBJETOS DE LOS MODELOS ESPECIFICADOS, LA
    # BUSQUEDA DE OBJETOS DEL MODELO "Description" SOLO TOMARA EL PRIMER REGISTRO, DEBIDO POR
    # EL MOMENTO ESTE MODELO SOLO CONTENDRA UN UNICO REGISTRO CON LA DESCRIPCION PERSONAL  
    description = Description.objects.first()
    experienciaA = ExperiencieA.objects.all()
    experienciaL = ExperiencieL.objects.all()
    s_i = skills_idiomas.objects.all()
    h_i = intereses_hobbies.objects.all().order_by('created')
    h_i_images = intereses_hobbies_images.objects.all()

    
    # VERIFICIAMOS QUE LOS OBJETOS ENCARARGADOS DE CONTENER LOS REGISTROS DE LA BASE DE DATOS
    # NO SE ENCUENTREN VACIOS (MENORES A CERO).
    if (experienciaA.count() != '0'):
        flag_EA = True

    if (experienciaL.count() != '0'):
        flag_EL = True

    if (s_i.count() != '0'):
        flag_L = True

    if (h_i.count() != '0'):
        flag_HI = True

    #RETORNAMOS LA INFORMACION CON EL NOMBRE DE LOS DICCIONARIOS A MANEJAR DENTRO DEL DOCUMENTO
    # "about.html"
    return render(request, 'about/about.html', {'descripcion':description,
                           'eAcademica':experienciaA,
                           'eLaboral':experienciaL,
                           'Skill_Idiomas':s_i,
                           'Hobbies_Intereses':h_i,
                           'Hobbies_Intereses_Images':h_i_images,
                           'EA_Any':flag_EA,
                           'EL_Any':flag_EL,
                           'L_Any': flag_L,
                           'HI_Any':flag_HI,
                           'LabelFontSize':label_font_size,
                           'HeaderFontSize':header_font_size,
                           'ExpFontSize':exp_font_size})
from django.shortcuts import render, HttpResponse

#===================================================================================
#===================================================================================
# Cada vista se corresponde con una funcion definida en la clase/fichero 'views.py'.
# Create your views (aka functions) here.
#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA PAGINA PRINCIPAL.
# RECIBE UN PARAMETRO DENOMINADO 'request' Y CONTIENE "Mucha Informacion".
def home(request):

    return render(request, "core/home.html")

#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION.

def about(request):

    return render(request, 'core/about.html')

#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION DE CONTACTO.

def contact(request):

    return render(request, 'core/contact.html')

#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION DE CONTACTO.

def portfolio(request):

    return render(request, 'core/portfolio.html')

from django.shortcuts import render, HttpResponse
#===================================================================================
#===================================================================================
#DEFINICION DE PAGINA BASE HTML
html_base = """
                <head>
                    <style>

                        h1 {
                            color:black;
                            text-align: center;
                        }

                        h2 {
                            color:black;
                            text-align: center;
                        }

                    </style>
                </head>

                <h1>MI WEB PERSONAL</h1>
                <p>Navegar:</p>
                <ul>
                    <li><a href = '/'>Pagina Princial</a></li>
                    <li><a href = '/about'>Acerca de</a></li>
                    <li><a href = '/contact'>Contacto<a/></li>
                </ul>"""

#===================================================================================
#===================================================================================
# Cada vista se corresponde con una funcion definida en la clase/fichero 'views.py'.
# Create your views (aka functions) here.
#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA PAGINA PRINCIPAL.
# RECIBE UN PARAMETRO DENOMINADO 'request' Y CONTIENE "Mucha Informacion".
def Home(request):

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
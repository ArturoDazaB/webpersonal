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

    html =  """ <h2>Bienvenido</h2>
                <p>Esta es la portada</p>"""

    return HttpResponse(html_base+html)

#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION.

def about(request):

    html =  """<h2>Acerca de:</h2>
            <p>Me llamo Arturo y me encanta Django!"""

    return HttpResponse(html_base+html)

#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA LA DE INFORMACION DE CONTACTO.

def contact(request):

    html =  """ <h2>Contacto:</h2>
                <p>Aqui dejo mi email y mis redes sociales</p>
                
                <ul>
                
                    <li><a href="mailto:carlos.arturo.dazab@gmail.com">Correo electronico</a></li>
                    <li><a href="https://www.facebook.com/CarlosDazaB/">Facebook</a></li>
                    <li><a href="https://github.com/ArturoDazaB">GitHub</a></li>

                </ul>"""

    return HttpResponse(html_base+html)
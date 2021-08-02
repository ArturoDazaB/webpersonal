"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from core import views as core_views
from portfolio.urls import portfolio_url
from about import views as about_view

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about-me/', about_view.about, name='about'),
    path('contact/', core_views.contact, name = 'contact'),
    path('portfolio/', include(portfolio_url)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# CUSTOM TITLES FOR ADMIN SITE
admin.site.site_header = "Carlos Arturo Daza Bohorquez - Web Personal"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "Carlos Arturo Daza Bohorquez"
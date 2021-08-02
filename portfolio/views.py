from about import models
from django.db.models.base import Model
from django.shortcuts import render
from .models import Project
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
#===================================================================================
#===================================================================================
# FUNCION QUE RETORNA EL PORTAFOLIO.

class PortfolioListView(ListView):
    model = Project

class PortfolioDetailView(DetailView):
    models = Project

#def portfolio(request):
#    projects = Project.objects.all()
#    return render(request, 'portfolio/portfolio.html', {'projects':projects})
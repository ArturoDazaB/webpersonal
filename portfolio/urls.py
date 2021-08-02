from django.urls import path
from .views import PortfolioListView, PortfolioDetailView

portfolio_url = ([
    path('', PortfolioListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', PortfolioDetailView.as_view(), name='project')
], 'portfolio')

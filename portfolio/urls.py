from django.urls import path
from .views import PortfolioListView

portfolio_url = ([path('', PortfolioListView.as_view(), name='projects')], 'portfolio')

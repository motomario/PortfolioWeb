from django.urls import path
from .views import index_view, scrapesheet_plotly, scrapesheet_seaborn, sales_analysis, siurblys_plots

urlpatterns = [
    path('', index_view, name='index'),
    path('scrapesheet_plotly.html', scrapesheet_plotly, name='scrapesheet_plotly'),
    path('scrapesheet_seaborn.html', scrapesheet_seaborn, name='scrapesheet_seaborn'),
    path('sales_analysis.html', sales_analysis, name='sales_analysis'),
    path('siurblys_plots.html', siurblys_plots, name='siurblys_plots')
]


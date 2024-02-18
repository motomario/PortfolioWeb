from django.urls import path
from .views import index_view, scrapesheet_plotly, scrapesheet_seaborn

urlpatterns = [
    path('', index_view, name='index'),
    path('scrapesheet_plotly.html', scrapesheet_plotly, name='scrapesheet_plotly'),
    path('scrapesheet_seaborn.html', scrapesheet_seaborn, name='scrapesheet_seaborn'),
]


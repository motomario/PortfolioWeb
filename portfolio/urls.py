from django.urls import path
from .views import index_view, scrapesheet_plotly, scrapesheet_seaborn, sales_analysis, siurblys_plots, tracking_pixel, track_link_click, export_tracking_stats

urlpatterns = [
    path('', index_view, name='index'),
    path('scrapesheet_plotly/', scrapesheet_plotly, name='scrapesheet_plotly'),
    path('scrapesheet_seaborn/', scrapesheet_seaborn, name='scrapesheet_seaborn'),
    path('sales_analysis/', sales_analysis, name='sales_analysis'),
    path('siurblys_plots/', siurblys_plots, name='siurblys_plots'),
    path('pixel/<uuid:tracking_id>.png', tracking_pixel, name='tracking_pixel'),
    path('track_link_click/<uuid:tracking_id>/', track_link_click, name='track_link_click'),
    path('export_tracking_stats/', export_tracking_stats, name='export_tracking_stats'),
]

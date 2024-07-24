from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('scrapesheet_plotly/', views.scrapesheet_plotly, name='scrapesheet_plotly'),
    path('scrapesheet_seaborn/', views.scrapesheet_seaborn, name='scrapesheet_seaborn'),
    path('sales_analysis/', views.sales_analysis, name='sales_analysis'),
    path('siurblys_plots/', views.siurblys_plots, name='siurblys_plots'),
    path('portfolio/image/<uuid:tracking_id>.png', views.tracking_pixel, name='tracking_pixel'),
    path('oocco/<uuid:tracking_id>/', views.track_link_click, name='track_link_click'),
    path('export_tracking_stats/', views.export_tracking_stats, name='export_tracking_stats'),
]

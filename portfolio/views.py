import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import EmailTracking
import csv
import uuid

logger = logging.getLogger(__name__)

def index_view(request):
    tracking_id = request.GET.get('tracking_id', str(uuid.uuid4()))
    return render(request, 'portfolio/index.html', {'tracking_id': tracking_id})

def scrapesheet_plotly(request):
    return render(request, 'portfolio/scrapesheet_plotly.html')

def scrapesheet_seaborn(request):
    return render(request, 'portfolio/scrapesheet_seaborn.html')

def sales_analysis(request):
    return render(request, 'portfolio/sales_analysis.html')

def siurblys_plots(request):
    return render(request, 'portfolio/siurblys_plots.html')

def tracking_pixel(request, tracking_id):
    logger.debug(f"Image requested for ID: {tracking_id}")
    tracking_entry = get_object_or_404(EmailTracking, tracking_id=tracking_id)
    tracking_entry.opened += 1
    tracking_entry.open_timestamp = timezone.now()
    tracking_entry.save()
    logger.debug(f"Updated tracking entry: {tracking_entry.email}, opened: {tracking_entry.opened}")

    with open('portfolio/static/portfolio/images/px.png', 'rb') as f:
        return HttpResponse(f.read(), content_type="image/png")

def track_link_click(request, tracking_id):
    logger.debug(f"Link clicked for ID: {tracking_id}")
    tracking_entry = get_object_or_404(EmailTracking, tracking_id=tracking_id)
    tracking_entry.clicked += 1
    tracking_entry.click_timestamp = timezone.now()
    tracking_entry.save()
    logger.debug(f"Updated tracking entry: {tracking_entry.email}, clicked: {tracking_entry.clicked}")

    return redirect('https://oocco.co.uk/')

def export_tracking_stats(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="email_tracking_stats.csv"'

    writer = csv.writer(response)
    writer.writerow(['Email', 'Tracking ID', 'Opened', 'Clicked', 'Open Timestamp', 'Click Timestamp'])

    for entry in EmailTracking.objects.all():
        writer.writerow([entry.email, entry.tracking_id, entry.opened, entry.clicked, entry.open_timestamp, entry.click_timestamp])

    return response

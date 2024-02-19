from django.shortcuts import render

def index_view(request):
    return render(request, 'portfolio/index.html')

def scrapesheet_plotly(request):
    return render(request, 'portfolio/scrapesheet_plotly.html')

def scrapesheet_seaborn(request):
    return render(request, 'portfolio/scrapesheet_seaborn.html')

def sales_analysis(request):
    return render(request, 'portfolio/sales_analysis.html')
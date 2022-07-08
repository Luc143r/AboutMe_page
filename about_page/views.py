from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.

def index_page(request):
    return render(request, 'about_page/index.html')

def aboutme_page(request):
    return render(request, 'about_page/about.html')

def portfolio_page(request):
    projects = Project.objects.all()
    return render(request, 'about_page/portfolio.html', {'projects': projects})

def contact_page(request):
    return render(request, 'about_page/contact.html')

def future_page(request):
    return render(request, 'about_page/future.html')
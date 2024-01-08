from django.shortcuts import render
from .models import Lead

# Create your views here.

def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request, "home.html", context)



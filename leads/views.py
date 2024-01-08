from django.shortcuts import render
from .models import Lead

# Home Page
def home_page(request):
    return render(request, "home.html")

# Leads Table Page
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }

    return render(request, "leads/lead_list.html", context)


# Lead Detail Page
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }
    return render(request, "leads/lead_detail.html", context)
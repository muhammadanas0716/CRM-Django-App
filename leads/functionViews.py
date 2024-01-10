from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadModelForm

# Home Page
def landing_page(request):
    return render(request, "landing.html")

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


# Lead Create Page
def lead_create(request):
    form = LeadModelForm() # returning a blank form
    if request.method == "POST":
        form = LeadModelForm(data=request.POST, initial={'first_name': 'John'})
        if form.is_valid():
            form.save()
            return redirect("/leads")
            
    context = {
        "form" : form
    }
    return render(request, "leads/lead_create.html", context)


# Lead Update Page
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(data=request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form":form,
        "lead":lead
    }
    return render(request, "leads/lead_update.html", context)

# Lead Delete Page
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
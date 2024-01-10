from django.shortcuts import reverse
from django.views.generic import (
TemplateView, 
ListView, 
DetailView, 
CreateView, 
UpdateView, 
DeleteView)
from .models import Lead
from .forms import LeadModelForm

# Landing Page View
class LandingPageView(TemplateView):
    template_name = "landing.html"

# Listing the Leads
class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


# Detail View of a Lead
class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

# Create a NEW Lead
class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
# Update an EXISITING Lead
class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# Delete a Lead
class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead-list")

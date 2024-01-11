from typing import Any
from django.shortcuts import reverse
from django.core.mail import send_mail
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
    
    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]),
        return super(LeadCreateView, self).form_valid(form)
    
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
    
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Lead
from .forms import LeadForm

class LeadListView(PermissionRequiredMixin, ListView):
    model = Lead
    template_name = "leads/lead_list.html"
    context_object_name = "leads"
    permission_required = "leads.view_lead"

class LeadDetailView(PermissionRequiredMixin, DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"
    permission_required = "leads.view_lead"

class LeadCreateView(PermissionRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = "leads/lead_form.html"
    success_url = "/lead/"
    permission_required = "leads.add_lead"

class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = "leads/lead_form.html"
    success_url = "/lead/"
    permission_required = "leads.change_lead"

class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = "leads/lead_confirm_delete.html"
    success_url = "/lead/"
    permission_required = "leads.delete_lead"

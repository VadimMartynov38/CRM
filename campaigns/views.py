from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Campaign
from .forms import CampaignForm

class CampaignListView(PermissionRequiredMixin, ListView):
    model = Campaign
    template_name = "campaigns/campaign_list.html"
    context_object_name = "campaigns"
    permission_required = "campaigns.view_campaign"

class CampaignDetailView(PermissionRequiredMixin, DetailView):
    model = Campaign
    template_name = "campaigns/campaign_detail.html"
    context_object_name = "campaign"
    permission_required = "campaigns.view_campaign"

class CampaignCreateView(PermissionRequiredMixin, CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = "campaigns/campaign_form.html"
    success_url = "/campaign/"
    permission_required = "campaigns.add_campaign"

class CampaignUpdateView(PermissionRequiredMixin, UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = "campaigns/campaign_form.html"
    success_url = "/campaign/"
    permission_required = "campaigns.change_campaign"

class CampaignDeleteView(PermissionRequiredMixin, DeleteView):
    model = Campaign
    template_name = "campaigns/campaign_confirm_delete.html"
    success_url = "/campaign/"
    permission_required = "campaigns.delete_campaign"

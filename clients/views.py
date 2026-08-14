from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Client
from .forms import ClientForm
from leads.models import Lead

class ClientListView(PermissionRequiredMixin, ListView):
    model = Client
    template_name = "clients/client_list.html"
    context_object_name = "clients"
    permission_required = "clients.view_client"

class ClientDetailView(PermissionRequiredMixin, DetailView):
    model = Client
    template_name = "clients/client_detail.html"
    context_object_name = "client"
    permission_required = "clients.view_client"

class ClientCreateView(PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/client_form.html"
    success_url = "/client/"
    permission_required = "clients.add_client"

    def get_initial(self):
        initial = super().get_initial()
        lead_id = self.request.GET.get("lead_id")

        if lead_id:
            try:
                lead = Lead.objects.get(pk=lead_id)
                initial.update({
                    "first_name": lead.first_name,
                    "last_name": lead.last_name,
                    "email": lead.email,
                    "phone": lead.phone,
                    "notes": lead.notes,
                })
                initial["status"] = Client.StatusChoices.ACTIVE
            except Lead.DoesNotExist:
                pass

        return initial

class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/client_form.html"
    success_url = "/client/"
    permission_required = "clients.change_client"

class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = "clients/client_confirm_delete.html"
    success_url = "/client/"
    permission_required = "clients.delete_client"

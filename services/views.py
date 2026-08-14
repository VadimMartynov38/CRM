from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Service
from .forms import ServiceForm

class ServiceListView(PermissionRequiredMixin, ListView):
    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"
    permission_required = "services.view_service"

class ServiceDetailView(PermissionRequiredMixin, DetailView):
    model = Service
    template_name = "services/service_detail.html"
    context_object_name = "service"
    permission_required = "services.view_service"

class ServiceCreateView(PermissionRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "services/service_form.html"
    success_url = "/service/"
    permission_required = "services.add_service"

class ServiceUpdateView(PermissionRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "services/service_form.html"
    success_url = "/service/"
    permission_required = "services.change_service"

class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
    model = Service
    template_name = "services/service_confirm_delete.html"
    success_url = "/service/"
    permission_required = "services.delete_service"

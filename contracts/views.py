from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Contract
from .forms import ContractForm

class ContractListView(PermissionRequiredMixin, ListView):
    model = Contract
    template_name = "contracts/contract_list.html"
    context_object_name = "contracts"
    permission_required = "contracts.view_contract"

class ContractDetailView(PermissionRequiredMixin, DetailView):
    model = Contract
    template_name = "contracts/contract_detail.html"
    context_object_name = "contract"
    permission_required = "contracts.view_contract"

class ContractCreateView(PermissionRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contract_form.html"
    success_url = "/contract/"
    permission_required = "contracts.add_contract"

class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contract_form.html"
    success_url = "/contract/"
    permission_required = "contracts.change_contract"

class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = "contracts/contract_confirm_delete.html"
    success_url = "/contract/"
    permission_required = "contracts.delete_contract"

from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContractListView.as_view(), name="contract_list"),
    path("<int:pk>/", views.ContractDetailView.as_view(), name="contract_detail"),
    path("create/", views.ContractCreateView.as_view(), name="contract_create"),
    path("<int:pk>/update/", views.ContractUpdateView.as_view(), name="contract_update"),
    path("<int:pk>/delete/", views.ContractDeleteView.as_view(), name="contract_delete"),
]

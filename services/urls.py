from django.urls import path
from . import views

urlpatterns = [
    path("", views.ServiceListView.as_view(), name="service_list"),
    path("<int:pk>/", views.ServiceDetailView.as_view(), name="service_detail"),
    path("create/", views.ServiceCreateView.as_view(), name="service_create"),
    path("<int:pk>/update/", views.ServiceUpdateView.as_view(), name="service_update"),
    path("<int:pk>/delete/", views.ServiceDeleteView.as_view(), name="service_delete"),
]

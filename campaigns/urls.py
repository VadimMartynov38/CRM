from django.urls import path
from . import views

urlpatterns = [
    path("", views.CampaignListView.as_view(), name="campaign_list"),
    path("<int:pk>/", views.CampaignDetailView.as_view(), name="campaign_detail"),
    path("create/", views.CampaignCreateView.as_view(), name="campaign_create"),
    path("<int:pk>/update/", views.CampaignUpdateView.as_view(), name="campaign_update"),
    path("<int:pk>/delete/", views.CampaignDeleteView.as_view(), name="campaign_delete"),
]

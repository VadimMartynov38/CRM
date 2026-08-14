from django.contrib import admin
from .models import Campaign

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "budget", "start_date", "end_date")
    list_filter = ("status", "start_date", "end_date")
    search_fields = ("name", "description")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "start_date"

from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone", "status", "source", "created_at")
    list_filter = ("status", "source", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "notes")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    list_editable = ("status",)

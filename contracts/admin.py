from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "type", "status", "amount", "start_date", "end_date")
    list_filter = ("type", "status", "start_date", "end_date")
    search_fields = ("number", "title", "notes")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    list_editable = ("status",)

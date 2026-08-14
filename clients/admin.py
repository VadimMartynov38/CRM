from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "status", "get_name", "email", "phone", "created_at")
    list_filter = ("type", "status", "created_at")
    search_fields = ("first_name", "last_name", "company_name", "email", "inn", "notes")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    list_editable = ("status",)

    @admin.display(description="Имя / Компания")
    def get_name(self, obj):
        if obj.type == Client.TypeChoices.COMPANY:
            return obj.company_name or f"Компания #{obj.pk}"
        name = f"{obj.first_name} {obj.last_name}".strip()
        return name or f"Частное лицо #{obj.pk}"

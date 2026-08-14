from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "type",
            "status",
            "first_name",
            "last_name",
            "company_name",
            "inn",
            "kpp",
            "email",
            "phone",
            "address",
            "notes",
        ]
        widgets = {
            "type": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "inn": forms.TextInput(attrs={"class": "form-control", "placeholder": "Например: 7701234567"}),
            "kpp": forms.TextInput(attrs={"class": "form-control", "placeholder": "Например: 770101001"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+7..."}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

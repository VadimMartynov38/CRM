from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ["name", "description", "budget", "start_date", "end_date", "status"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Название кампании"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "budget": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }

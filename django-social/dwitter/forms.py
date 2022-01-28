from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Escreva seu Dweet...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
        error_messages={'max_length':'Este dweet está muito longo! Observe o limite de 140 caracteres.'}
    )

    class Meta:
        model = Dweet
        exclude = ("user", )

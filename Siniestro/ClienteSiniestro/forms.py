from django import forms
from .models import Sinis

class SinisForm(forms.ModelForm):
    class Meta:
        model = Sinis
        fields = '__all__'
        exclude = ['imagen1', 'imagen2', 'imagen3', 'imagen4', 'imagen5',
                   'expli1', 'expli2', 'expli3', 'expli4', 'expli5']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }

class EvidForm(forms.ModelForm):
    class Meta:
        model = Sinis
        fields = [
            "imagen1", "expli1",
            "imagen2", "expli2",
            "imagen3", "expli3",
            "imagen4", "expli4",
            "imagen5", "expli5",
        ]
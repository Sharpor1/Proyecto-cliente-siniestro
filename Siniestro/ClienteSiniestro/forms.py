from django import forms
from .models import Sinis

class SinisForm(forms.ModelForm):
    
    class Meta:
        model = Sinis
        fields = '__all__'
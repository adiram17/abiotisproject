from .models import Abiotis
from django import forms
from django.forms import ModelForm

class AbiotisForm(ModelForm):
    class Meta:
        model = Abiotis
        fields = ('selection','origin', 'type', 'umur_jagung_jantan', 'umur_jagung_betina', 'umur_panen')
        widgets = {
            'selection': forms.Select(attrs={'class':'form-control'}),
            'origin': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.TextInput(attrs={'class':'form-control', 'readonly': 'true'}),
            'origin': forms.TextInput(attrs={'class':'form-control'}),
            'umur_jagung_jantan': forms.TextInput(attrs={'class':'form-control'}),
            'umur_jagung_betina': forms.TextInput(attrs={'class':'form-control'}),
            'umur_panen': forms.TextInput(attrs={'class':'form-control'}),
            
        }
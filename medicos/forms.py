from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'especialidade', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'crm': forms.TextInput(attrs={'class':'form-control'}),
            'especialidade': forms.TextInput(attrs={'class':'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

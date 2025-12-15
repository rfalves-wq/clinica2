from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # Inclui apenas campos que existem no modelo
        fields = ['nome', 'nome_mae','nome_pai','idade', 'telefone', 'ativo', 'cpf']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }

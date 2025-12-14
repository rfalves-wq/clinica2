from django import forms
from .models import Triagem

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = [
            'paciente',
            'enfermeiro',
            'pressao_arterial',
            'temperatura',
            'frequencia_cardiaca',
            'classificacao',
            'observacoes'
        ]

from django import forms
from .models import Atendimento
from enfermeiros.models import Enfermeiro

class TriagemForm(forms.ModelForm):
    enfermeiro = forms.ModelChoiceField(
        queryset=Enfermeiro.objects.filter(ativo=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Enviar para Enfermeiro'
    )

    class Meta:
        model = Atendimento
        fields = ['enfermeiro']

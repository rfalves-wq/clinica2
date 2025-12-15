from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enfermeiros.models import Enfermeiro
from .models import Triagem

@login_required
def painel_triagem(request):
    try:
        enfermeiro = Enfermeiro.objects.get(user=request.user)
    except Enfermeiro.DoesNotExist:
        return render(request, 'triagem/sem_perfil.html')

    triagens = Triagem.objects.filter(
        enfermeiro=enfermeiro,
        finalizada=False
    )

    return render(request, 'triagem/painel.html', {
        'triagens': triagens
    })

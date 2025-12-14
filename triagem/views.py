from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Triagem

@login_required
def painel_triagem(request):
    enfermeiro = request.user.enfermeiro

    triagens = Triagem.objects.filter(
        enfermeiro=enfermeiro,
        finalizada=False
    )

    return render(request, 'triagem/painel.html', {
        'triagens': triagens
    })

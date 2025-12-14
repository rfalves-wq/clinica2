from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from pacientes.models import Paciente
from enfermeiros.models import Enfermeiro
from triagem.models import Triagem

@login_required
def recepcao_busca(request):
    query = request.GET.get('q', '')
    pacientes = []
    enfermeiros = Enfermeiro.objects.all()

    if query:
        pacientes = Paciente.objects.filter(
            Q(nome__icontains=query) |
            Q(cpf__icontains=query)
        )

    return render(request, 'recepcao/busca.html', {
        'pacientes': pacientes,
        'enfermeiros': enfermeiros,
        'query': query
    })


@login_required
def enviar_para_triagem(request, paciente_id):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, id=paciente_id)
        enfermeiro_id = request.POST.get('enfermeiro')

        enfermeiro = get_object_or_404(Enfermeiro, id=enfermeiro_id)

        Triagem.objects.create(
            paciente=paciente,
            enfermeiro=enfermeiro
        )

    return redirect('recepcao_busca')

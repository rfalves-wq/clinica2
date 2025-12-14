from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enfermeiro
from .forms import EnfermeiroForm
from django.contrib.auth.decorators import login_required

@login_required
def enfermeiros_list(request):
    enfermeiros = Enfermeiro.objects.all()
    return render(request, 'enfermeiros/list.html', {'enfermeiros': enfermeiros})

@login_required
def enfermeiros_add(request):
    if request.method == 'POST':
        form = EnfermeiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enfermeiros_list')
    else:
        form = EnfermeiroForm()
    return render(request, 'enfermeiros/form.html', {'form': form, 'titulo': 'Adicionar Enfermeiro'})

@login_required
def enfermeiros_edit(request, id):
    enfermeiro = get_object_or_404(Enfermeiro, id=id)
    if request.method == 'POST':
        form = EnfermeiroForm(request.POST, instance=enfermeiro)
        if form.is_valid():
            form.save()
            return redirect('enfermeiros_list')
    else:
        form = EnfermeiroForm(instance=enfermeiro)
    return render(request, 'enfermeiros/form.html', {'form': form, 'titulo': 'Editar Enfermeiro'})

@login_required
def enfermeiros_delete(request, id):
    enfermeiro = get_object_or_404(Enfermeiro, id=id)
    enfermeiro.delete()
    return redirect('enfermeiros_list')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recepcao.models import Atendimento

@login_required
def painel_triagem(request):
    atendimentos = Atendimento.objects.filter(
        status__in=['AGUARDANDO', 'EM_TRIAGEM']
    ).order_by('chegada')

    return render(request, 'enfermeiros/painel_triagem.html', {
        'atendimentos': atendimentos
    })


@login_required
def iniciar_triagem(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, id=atendimento_id)
    atendimento.status = 'EM_TRIAGEM'
    atendimento.save()
    return redirect('painel_triagem')


@login_required
def finalizar_triagem(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, id=atendimento_id)
    atendimento.status = 'FINALIZADO'
    atendimento.save()
    return redirect('painel_triagem')

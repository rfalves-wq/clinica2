from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from .forms import MedicoForm

def medicos_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/list.html', {'medicos': medicos})

def medicos_add(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicos_list')
    else:
        form = MedicoForm()
    return render(request, 'medicos/form.html', {'form': form, 'titulo': 'Adicionar Médico'})

def medicos_edit(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medicos_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'medicos/form.html', {'form': form, 'titulo': 'Editar Médico'})

def medicos_delete(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect('medicos_list')

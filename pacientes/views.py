from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

# Listagem
def pacientes_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/list.html', {'pacientes': pacientes})

# Adicionar
def pacientes_add(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes_list')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form, 'titulo': 'Adicionar Paciente'})

# Editar
def pacientes_edit(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form.html', {'form': form, 'titulo': 'Editar Paciente'})

# Excluir
def pacientes_delete(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('pacientes_list')


from django.shortcuts import render, get_object_or_404
from .models import Paciente

def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'pacientes/paciente_detail.html', {
        'paciente': paciente
    })

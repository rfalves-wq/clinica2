from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm

# =========================
# LOGIN / LOGOUT / HOME
# =========================

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'accounts/home.html')

# =========================
# CRUD USUÁRIOS
# =========================

@login_required
def users_list(request):
    users = User.objects.all()
    return render(request, 'accounts/users_list.html', {'users': users})

@login_required
def users_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Criptografa a senha
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('users_list')
    else:
        form = UserForm()
    return render(request, 'accounts/users_form.html', {'form': form, 'titulo': 'Adicionar Usuário'})

@login_required
def users_edit(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('users_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'accounts/users_form.html', {'form': form, 'titulo': 'Editar Usuário'})

@login_required
def users_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users_list')

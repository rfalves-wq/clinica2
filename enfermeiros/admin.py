from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Enfermeiro

@admin.register(Enfermeiro)
class EnfermeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'coren', 'setor', 'ativo', 'user')
    search_fields = ('nome', 'coren')

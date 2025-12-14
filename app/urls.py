from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticação / Home
    path('', include('accounts.urls')),

    # Cadastros
    path('medicos/', include('medicos.urls')),
    path('enfermeiros/', include('enfermeiros.urls')),
    path('pacientes/', include('pacientes.urls')),

    # Recepção e Triagem
    path('recepcao/', include('recepcao.urls')),
    path('triagem/', include('triagem.urls')),

    # Fallback
    path('', RedirectView.as_view(url='/home/')),
]

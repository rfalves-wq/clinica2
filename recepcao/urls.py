from django.urls import path
from . import views

urlpatterns = [
    path('', views.recepcao_busca, name='recepcao_busca'),
    path(
        'enviar-triagem/<int:paciente_id>/',
        views.enviar_para_triagem,
        name='enviar_para_triagem'
    ),
]

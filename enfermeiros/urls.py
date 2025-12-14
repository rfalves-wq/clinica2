from django.urls import path
from . import views

urlpatterns = [
    path('', views.enfermeiros_list, name='enfermeiros_list'),
    path('add/', views.enfermeiros_add, name='enfermeiros_add'),
    path('edit/<int:id>/', views.enfermeiros_edit, name='enfermeiros_edit'),
    path('delete/<int:id>/', views.enfermeiros_delete, name='enfermeiros_delete'),
    
    path('triagem/', views.painel_triagem, name='painel_triagem'),
    path('triagem/iniciar/<int:atendimento_id>/', views.iniciar_triagem, name='iniciar_triagem'),
    path('triagem/finalizar/<int:atendimento_id>/', views.finalizar_triagem, name='finalizar_triagem'),


]

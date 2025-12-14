from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicos_list, name='medicos_list'),
    path('add/', views.medicos_add, name='medicos_add'),
    path('edit/<int:id>/', views.medicos_edit, name='medicos_edit'),
    path('delete/<int:id>/', views.medicos_delete, name='medicos_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes_list, name='pacientes_list'),
    path('add/', views.pacientes_add, name='pacientes_add'),
    path('edit/<int:id>/', views.pacientes_edit, name='pacientes_edit'),
    path('delete/<int:id>/', views.pacientes_delete, name='pacientes_delete'),
]

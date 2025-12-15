from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel_triagem, name='painel_triagem'),
    
]

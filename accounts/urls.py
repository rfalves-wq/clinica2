from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),

    # CRUD usuários
    path('users/', views.users_list, name='users_list'),
    path('users/add/', views.users_add, name='users_add'),
    path('users/edit/<int:id>/', views.users_edit, name='users_edit'),
    path('users/delete/<int:id>/', views.users_delete, name='users_delete'),
]

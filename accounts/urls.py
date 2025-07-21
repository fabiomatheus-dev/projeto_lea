from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),  # Alterado para já ir direto para o login
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset, name='password_reset'),
]

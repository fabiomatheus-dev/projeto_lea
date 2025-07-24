from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_configuracoes, name='tela_configuracoes'),  # Tela ao clicar na engrenagem
]

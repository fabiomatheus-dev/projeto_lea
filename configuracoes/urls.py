from django.urls import path
from . import views

urlpatterns = [
    path('configuracoes/', views.tela_configuracoes, name='configuracoes'),  # Tela ao clicar na engrenagem
]

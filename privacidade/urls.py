from django.urls import path
from . import views

urlpatterns = [
    path('privacidade/', views.privacidade, name='privacidade'),
]

from django.shortcuts import render

def lea_app(request):
    return render(request, 'lea_app/index.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def password_reset(request):
    return render(request, 'password_reset.html')

def privacidade(request):
    return render(request, 'privacidade.html')

def tela_configuracoes(request):
    return render(request, 'tela_configuracoes.html')

def interacao(request):
    return render(request, 'interacao.html')
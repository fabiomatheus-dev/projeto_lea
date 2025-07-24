from django.shortcuts import render

def tela_configuracoes(request):
    return render(request, 'configuracoes.html')


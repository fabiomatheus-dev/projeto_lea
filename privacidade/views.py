from django.shortcuts import render

def privacidade(request):
    return render(request, 'privacidade/privacidade.html')

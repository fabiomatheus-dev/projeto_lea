from django.shortcuts import render

def index(request):
    return render(request, 'lea_app/index.html')

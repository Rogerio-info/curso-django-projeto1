from django.shortcuts import render, HttpResponse

# Create your views here.


def contato(request):
    return HttpResponse('Contato')

def home(request):
    return render(request,'recipes/home.html')

def sobre(request):
    return HttpResponse('Sobre')

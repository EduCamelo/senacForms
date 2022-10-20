from django.shortcuts import render
from viagens.forms import ViagemForms

def index(request):
    form= ViagemForms()
    contexto= {'form' : form}
    return render(request, 'index.html', contexto)

def revConsulta(request):
    if request.method == 'POST':
        form = ViagemForms(request.POST)
        contexto={'form' : form}
        return render (request, 'consulta.html', contexto)

def base(request):
    return render(request,'base.html')

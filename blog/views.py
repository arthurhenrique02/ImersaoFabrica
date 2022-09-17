from django.shortcuts import render, redirect
from django.http import HttpResponse
# importar as classes
from .models import Contatos
from .forms import  formulario


# Create your views here.
def home(request):
    contats = Contatos.objects.all()
    data = {}
    data['contats'] = contats
    return render(request, 'blog/home.html', data)

# criação de um novo contato
def novo_contato(request):
    form = formulario(request.POST or None)
    # definir um dicionario para armazenar as infos
    data = {}
    data['form'] = form
    
    # verificar o conteudo criado
    if form.is_valid():
        form.save()
        return redirect('home')
  
    return render(request, 'blog\create.html', data)

# ver o contato criado
def ver_contato(request, pk):
    # pegar a primary key
    contato = Contatos.objects.get(pk = pk)
    data = {}
    data['contato'] = contato

    return render(request, 'blog/contato.html', data)

# atualizar/deletar o contato criado
def update(request, pk):
    contato = Contatos.objects.get(pk = pk) 
    form = formulario(request.POST or None, instance = contato)
    data = {}
    data['contato'] = contato
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'blog/update.html', data)

def delete(request, pk):
    contato = Contatos.objects.get(pk = pk)
    contato.delete()

    return redirect('home')

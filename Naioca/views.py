from django.shortcuts import render
from django.http import HttpResponse

def telainicial(request):
    return render(request,"Naioca/tela_inicial.html")

def login(request):
    return render(request,"Naioca/pagina_de_login.html")

def sobre(request):
    return render(request,"Naioca/sobre.html")

def tela_inicial(request):
    itens = [
        {"nome": "Bolo de chocolate", "descricao": "Bolo de chocolate delicioso e fofinho."},
        {"nome": "Bolo de limão", "descricao": "Bolo de limão refrescante e azedinho."},
        {"nome": "Bolo de cenoura", "descricao": "Bolo de cenoura com cobertura de chocolate."},
    ]
    return render(request, "Naioca/tela_inicial.html", {"itens": itens})

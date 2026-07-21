from django.shortcuts import render
from django.http import HttpResponse

def telainicial(request):
    return render(request,"Naioca/telainicial.html")

def login(request):
    return render(request,"Naioca/login.html")

def sobre(request):
    return render(request,"Naioca/sobre.html")

def cardapio(request):
    return cardapio(request,"Naioca/cardapio.html")

def criarconta(request):
    return render(request,"Naioca/criarconta.html")

def menu(request):
    itens = [
        {"nome": "Bolo de chocolate", "descricao": "Bolo de chocolate delicioso e fofinho."},
        {"nome": "Bolo de limão", "descricao": "Bolo de limão refrescante e azedinho."},
        {"nome": "Bolo de cenoura", "descricao": "Bolo de cenoura com cobertura de chocolate."},
    ]
    context = {
        "itens": itens
    }
    return render(request, "Naioca/cardapio.html", context)

def pagamento(request):
    return render(request, "Naioca/pagamento.html")
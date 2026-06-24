from django.shortcuts import render
from django.http import HttpResponse

def telainicial(request):
    return render(request,"Naioca/tela_inicial.html")

def paginadelogin(request):
    return render(request,"Naioca/pagina_de_login.html")

def sobre(request):
    return render(request,"Naioca/sobre.html")

def tela_inicial(request):
    itens = [
        {"nome": "Bolo de chocolate", "descricao": "Bolo de chocolate delicioso e fofinho."},
        {"nome": "Item 2", "descricao": "Descrição do Item 2"},
        {"nome": "Item 3", "descricao": "Descrição do Item 3"},
    ]
    return render(request, "Naioca/tela_inicial.html", {"itens": itens})

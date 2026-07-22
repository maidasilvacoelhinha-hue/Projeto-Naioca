from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Pedido

def telainicial(request):
    return render(request,"Naioca/telainicial.html")

def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        senha = request.POST.get("senha")

        try:

            cliente = Cliente.objects.get(
                email=email,
                senha=senha
            )

            request.session["cliente"] = cliente.id

            return redirect("Naioca:cardapio")

        except Cliente.DoesNotExist:

            return render(request,
                          "Naioca/login.html",
                          {"erro":"Email ou senha inválidos."})

    return render(request, "Naioca/login.html")

def sobre(request):
    return render(request,"Naioca/sobre.html")

def cardapio(request):
    itens = [
        {"nome": "Brownie Clássico", "preco": 8},
        {"nome": "Brownie com Ninho", "preco": 12},
        {"nome": "Brownie Brigadeiro", "preco": 12},
        {"nome": "Brownie Doce de Leite", "preco": 13},
        {"nome": "Brownie Oreo", "preco": 13},
    ]

    return render(request, "Naioca/cardapio.html", {"itens": itens})

def criarconta(request):

    if request.method == "POST":

        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if Cliente.objects.filter(email=email).exists():

            return render(request,
                          "Naioca/criarconta.html",
                          {"erro":"Este e-mail já está cadastrado."})

        Cliente.objects.create(
            nome=nome,
            email=email,
            senha=senha
        )

        return redirect("Naioca:login")

    return render(request, "Naioca/criarconta.html")

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

    total = request.GET.get("total", "0")

    if request.method == "POST":

        cep = request.POST.get("cep")
        rua = request.POST.get("rua")
        bairro = request.POST.get("bairro")
        forma = request.POST.get("forma_pagamento")

        cliente_id = request.session.get("cliente")

        cliente = None

        if cliente_id:
            cliente = Cliente.objects.get(id=cliente_id)

        pedido = Pedido.objects.create(
            cliente=cliente,
            cep=cep,
            rua=rua,
            bairro=bairro,
            forma_pagamento=forma,
            total=total
        )

        return render(
            request,
            "Naioca/pedido_recebido.html",
            {
                "total": total,
                "forma": forma,
                "pedido": pedido
            }
        )

    return render(
        request,
        "Naioca/pagamento.html",
        {
            "total": total
        }
    )

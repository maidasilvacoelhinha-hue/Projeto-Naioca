from django.shortcuts import render
from django.http import HttpResponse

def telainicial(request):
    return render(request,"Naioca/tela_inicial.html")

def paginadelogin(request):
    return render(request,"Naioca/pagina_de_login.html")

def sobre(request):
    return render(request,"Naioca/sobre.html")


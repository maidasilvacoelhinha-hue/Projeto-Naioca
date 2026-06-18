from django.shortcuts import render
from django.http import HttpResponse

def telainicial(request):
    return HttpResponse("tela inicial")

def paginadelogin(request):
    return HttpResponse("pagina de login")

def sobre(request):
    return HttpResponse("sobre")


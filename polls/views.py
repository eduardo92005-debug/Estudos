from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Home index")

def detail(request, pergunta_id):
    return HttpResponse('Na tela de perguntas %s' % pergunta_id)

def resultados(request, pergunta_id):
    response = "Na view de resultados %s"
    return HttpResponse(response % pergunta_id)

def vote(request, pergunta_id):
    return HttpResponse('Página de voto %s' % pergunta_id)
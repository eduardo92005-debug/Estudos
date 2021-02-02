from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    texto_index = "Tela de index"
    return HttpResponse(texto_index)


def perguntas(request, pergunta_id):
    return HttpResponse('Na tela de pergunta')

def resposta(request, pergunta_id):
    return HttpResponse('Na tela de resposta')
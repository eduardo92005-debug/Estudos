from django.urls import path

from .views import index, perguntas, resposta

urlpatterns = [
    path('/', index, name='index'),
    path('/perguntas/<int:pergunta_id>/', perguntas, name='pergunta'),
    #path('/<int:pergunta_id>/', views.detail, name='detail'),
    path('/perguntas/<int:pergunta_id>/resposta', resposta, name='resposta'),
]

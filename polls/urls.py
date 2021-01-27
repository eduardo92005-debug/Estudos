from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pergunta_id>/', views.detail, name='detail'),
    path('<int:pergunta_id>/resultados/', views.resultados, name ='resultados'),
    path('<int:pergunta_id>/vote/',views.vote, name='vote'),
]
from django.db import models
from datetime import datetime

# Create your models here.


class Pergunta(models.Model):
    pergunta_texto = models.CharField(
        max_length=200, blank=False, unique=True, default=None)
    pub_date = models.DateTimeField(
        default=datetime.now(), name='Data de publicacao')

    def __str__(self):
        return self.pergunta_texto


class Opcoe(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.PROTECT)
    OPCAO_A = 'A'
    OPCAO_B = 'B'
    OPCAO_C = 'C'
    OPCAO_D = 'D'
    OPCAO_E = 'E'
    TLISTA_OPCOES = [(OPCAO_A, 'A'), (OPCAO_B, 'B'),
                     (OPCAO_C, 'C'), (OPCAO_D, 'D'), (OPCAO_E, 'E')]
    md_opcoes = models.CharField(
        max_length=1,
        choices=TLISTA_OPCOES, name='Escolha uma alternativa', default=OPCAO_A, blank=False)


class Respostas(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.PROTECT)
    #escolha_texto = models.CharField(max_length=200, blank=False, unique=True, name = 'Texto escolhido')
    votes = models.IntegerField(default=0, blank=False, name='Votos')

    def __str__(self):
        return self.escolha_texto


class Modos(models.Model):
    modo = models.CharField(max_length=20)

    def __str__(self):
        return self.modo

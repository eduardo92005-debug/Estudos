from django.db import models

# Create your models here.
class Perguntas(models.Model):
    pergunta_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.pergunta_texto

class Escolhas(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.escolha_texto

class Modos(models.Model):
    modo = models.CharField(max_length=20)
    def __str__(self):
        return self.modo
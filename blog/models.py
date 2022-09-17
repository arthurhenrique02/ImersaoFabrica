from django.db import models

# Create your models here.
class Contatos(models.Model):
    nome =  models.CharField(max_length=80)
    numero = models.CharField(max_length = 15)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    casa = models.IntegerField()
    ponto_ref = models.CharField(max_length=300)
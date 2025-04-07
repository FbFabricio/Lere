from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    carro = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    '''configurar para pegar data atual do cadastro'''

    def __str__(self):
        return f"{self.nome} - {self.carro} ({self.placa})"
    
    
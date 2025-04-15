from django.db import models
from django.utils.timezone import now



# Create your models here.
class Cliente(models.Model):


    nome = models.CharField(max_length=100)
    carro = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    servicos = models.TextField(default=1000)
    Data_entrada = models.DateField(default=now)
    

    def __str__(self):
        return f"{self.nome} - {self.carro} ({self.placa})"
    
    
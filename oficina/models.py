from django.db import models
from django.utils import timezone



# Create your models here.
class Cliente(models.Model):
    data_atual = timezone.now()
    nome = models.CharField(max_length=100)
    carro = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    Data_entrada = models.DateField(default=data_atual)
    

    def __str__(self):
        return f"{self.nome} - {self.carro} ({self.placa})"
    
    
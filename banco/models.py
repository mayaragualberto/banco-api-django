from django.db import models

# Create your models here.
class Cliente(models.Model):
  nome = models.CharField(max_length=32);
  cpf = models.CharField(max_length=11);

  def __str__(self):
    return self.nome


class Saque(models.Model):
  cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
  valor = models.FloatField()

class Deposito(models.Model):
  cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
  valor = models.FloatField()


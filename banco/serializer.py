from rest_framework import serializers
from banco.models import Cliente, Saque, Deposito

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = ['id', 'nome', 'cpf']

class SaqueSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Saque
        fields = ('__all__')


class DepositoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Deposito
        fields = ('__all__')
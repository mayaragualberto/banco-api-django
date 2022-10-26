from rest_framework import viewsets,status
from banco.models import Cliente
from banco.serializer import ClienteSerializer, SaqueSerializer, DepositoSerializer



# Create your views here.
class ClientesViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer


class SaquesViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = SaqueSerializer

class DepositosViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = DepositoSerializer
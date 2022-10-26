from django.contrib import admin
from banco.models import Cliente, Deposito, Saque

# Register your models here.
from .models import (
    Cliente,
    Deposito,
    Saque,
)

admin.site.register(Cliente)
admin.site.register(Deposito)
admin.site.register(Saque)
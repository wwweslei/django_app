from django.shortcuts import render
from .models import Veiculo, Cliente, Servicos


def home(request):
    veiculos = Veiculo.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'core/index.html', {'veiculos': veiculos, 'clientes': clientes.values_list})




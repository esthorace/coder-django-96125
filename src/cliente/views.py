from django.shortcuts import render

from cliente.models import Cliente


def index(request):
    cliente = Cliente.objects.all()
    contexto = {"clientes": cliente}
    return render(request, "cliente/index.html", contexto)

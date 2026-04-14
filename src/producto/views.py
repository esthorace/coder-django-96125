from django.shortcuts import render
from producto.models import CategoriaProducto


def index(request):
    query = CategoriaProducto.objects.all()
    contexto = {"productos": query}
    return render(request, "producto/index.html", contexto)

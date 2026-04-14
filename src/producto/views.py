from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from producto.models import CategoriaProducto
from producto.forms import CategoriaProductoForm


def index(request: HttpRequest):
    consulta = request.GET.get("consulta")
    if consulta:
        query = CategoriaProducto.objects.filter(nombre__contains=consulta)
    else:
        query = CategoriaProducto.objects.all()
    contexto = {"productos": query}
    return render(request, "producto/index.html", contexto)


def categoriaproducto_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = CategoriaProductoForm()
        contexto = {"form": form}
    if request.method == "POST":
        form = CategoriaProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    return render(request, "producto/categoriaproducto_form.html", contexto)


def categoriaproducto_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = CategoriaProducto.objects.get(id=pk)
    return render(
        request, "producto/categoriaproducto_detail.html", {"categoria": query}
    )


def categoriaproducto_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = CategoriaProducto.objects.get(id=pk)
    if request.method == "GET":
        form = CategoriaProductoForm(instance=query)
    if request.method == "POST":
        form = CategoriaProductoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    return render(request, "producto/categoriaproducto_form.html", {"form": form})

from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from producto.models import CategoriaProducto
from producto.forms import CategoriaProductoForm
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    ListView,
)


# def index(request: HttpRequest):
#     consulta = request.GET.get("consulta")
#     if consulta:
#         query = CategoriaProducto.objects.filter(nombre__contains=consulta)
#     else:
#         query = CategoriaProducto.objects.all()
#     contexto = {"productos": query}
#     return render(request, "producto/index.html", contexto)


class CategoriaProductoList(ListView):
    model = CategoriaProducto

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            query = CategoriaProducto.objects.filter(nombre__contains=consulta)
        else:
            query = CategoriaProducto.objects.all()
        return query


# def categoriaproducto_create(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         form = CategoriaProductoForm()
#         contexto = {"form": form}
#     if request.method == "POST":
#         form = CategoriaProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:index")
#     return render(request, "producto/categoriaproducto_form.html", contexto)


class CategoriaProductoCreate(CreateView):
    model = CategoriaProducto
    form_class = CategoriaProductoForm
    success_url = reverse_lazy("producto:index")


# def categoriaproducto_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     query = CategoriaProducto.objects.get(id=pk)
#     return render(
#         request, "producto/categoriaproducto_detail.html", {"categoria": query}
#     )


class CategoriaProductoDetail(DetailView):
    model = CategoriaProducto


# def categoriaproducto_update(request: HttpRequest, pk: int) -> HttpResponse:
#     query = CategoriaProducto.objects.get(id=pk)
#     if request.method == "GET":
#         form = CategoriaProductoForm(instance=query)
#     if request.method == "POST":
#         form = CategoriaProductoForm(request.POST, instance=query)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:index")
#     return render(request, "producto/categoriaproducto_form.html", {"form": form})


class CategoriaProductoUpdate(UpdateView):
    model = CategoriaProducto
    form_class = CategoriaProductoForm
    success_url = reverse_lazy("producto:index")


# def categoriaproducto_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     query = CategoriaProducto.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect("producto:index")
#     return render(
#         request, "producto/categoriaproducto_confirm_delete.html", {"categoria": query}
#     )

class CategoriaProductoDelete(DeleteView):
    model = CategoriaProducto
    success_url = reverse_lazy("producto:index")
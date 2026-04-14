from django.urls import path

from producto import views

app_name = "producto"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "categoriaproducto/create",
        views.categoriaproducto_create,
        name="categoriaproducto_create",
    ),
    path(
        "categoriaproducto/detail/<int:pk>",
        views.categoriaproducto_detail,
        name="categoriaproducto_detail",
    ),
    path(
        "categoriaproducto/update/<int:pk>",
        views.categoriaproducto_update,
        name="categoriaproducto_update",
    ),

]

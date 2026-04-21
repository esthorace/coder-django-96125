from django.urls import path

from producto import views

app_name = "producto"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.CategoriaProductoList.as_view(), name="index"),
    # path(
    #     "categoriaproducto/create",
    #     views.categoriaproducto_create,
    #     name="categoriaproducto_create",
    # ),
    path(
        "categoriaproducto/create",
        views.CategoriaProductoCreate.as_view(),
        name="categoriaproducto_create",
    ),
    # path(
    #     "categoriaproducto/detail/<int:pk>",
    #     views.categoriaproducto_detail,
    #     name="categoriaproducto_detail",
    # ),
    path(
        "categoriaproducto/detail/<int:pk>",
        views.CategoriaProductoDetail.as_view(),
        name="categoriaproducto_detail",
    ),
    # path(
    #     "categoriaproducto/update/<int:pk>",
    #     views.categoriaproducto_update,
    #     name="categoriaproducto_update",
    # ),
    path(
        "categoriaproducto/update/<int:pk>",
        views.CategoriaProductoUpdate.as_view(),
        name="categoriaproducto_update",
    ),
    # path(
    #     "categoriaproducto/delete/<int:pk>",
    #     views.categoriaproducto_delete,
    #     name="categoriaproducto_delete",
    # ),
    path(
        "categoriaproducto/delete/<int:pk>",
        views.CategoriaProductoDelete.as_view(),
        name="categoriaproducto_delete",
    ),
    # Rutas para Producto
    path(
        "producto/",
        views.ProductoList.as_view(),
        name="producto_list",
    ),
    path(
        "producto/<int:pk>/",
        views.ProductoDetail.as_view(),
        name="producto_detail",
    ),
    path(
        "producto/create/",
        views.ProductoCreate.as_view(),
        name="producto_create",
    ),
    path(
        "producto/<int:pk>/update/",
        views.ProductoUpdate.as_view(),
        name="producto_update",
    ),
    path(
        "producto/<int:pk>/delete/",
        views.ProductoDelete.as_view(),
        name="producto_delete",
    ),
]

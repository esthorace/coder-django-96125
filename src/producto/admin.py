from django.contrib import admin

from producto import models

admin.site.register(models.CategoriaProducto)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nombre", "stock", "unidad_medida", "precio")
    list_filter = ("categoria", "unidad_medida")
    search_fields = ("nombre", "categoria__nombre")

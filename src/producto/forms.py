from django import forms

from producto import models

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = models.CategoriaProducto
        fields = ["nombre", "descripcion"]


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["categoria", "nombre", "descripcion", "unidad_medida", "stock", "precio"]
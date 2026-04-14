from django import forms

from producto import models

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = models.CategoriaProducto
        fields = ["nombre", "descripcion"]
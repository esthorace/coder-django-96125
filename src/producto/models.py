from django.db import models

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"

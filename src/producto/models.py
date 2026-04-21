from django.db import models


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"


class Producto(models.Model):
    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="categoría",
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    unidad_medida = models.CharField(max_length=50)
    stock = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.unidad_medida}) ${self.precio}"

    class Meta:
        verbos_name = "Producto"
        verbos_name_plural = "Productos"
        unique_together = ("categoria", "producto")

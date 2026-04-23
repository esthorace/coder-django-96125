from decimal import Decimal
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Vendedor(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="vendedor"
    )
    celular = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    producto = models.ForeignKey("producto.Producto", on_delete=models.PROTECT)
    cantidad = models.FloatField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_venta",)

    def clean(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError(
                "La cantidad vendida no puede ser superior a la disponible"
            )

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * Decimal(str(self.cantidad))
        self.producto.stock -= self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)

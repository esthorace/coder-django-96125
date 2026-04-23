from django.contrib.auth.models import User
from django.db import models


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

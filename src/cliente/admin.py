from django.contrib import admin

# Register your models here.
from cliente import models

admin.site.register(models.Pais)
admin.site.register(models.Cliente)
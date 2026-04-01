from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("saludar/", views.saludar, name="saludar"),
    path("saludar2/", views.saludar2, name="saludar2"),
    path("saludar3/<str:nombre>/<str:apellido>/", views.saludar3, name="saludar3"),
    path("dados/", views.tirar_dado, name="dados"),
    path("notas/", views.ver_notas, name="notas"),
    path("usuarios/", views.ver_usuarios, name="usuarios"),
]

from django.urls import path

from cliente import views

app_name = "cliente"

urlpatterns = [
    path("", views.index, name="index"),
]

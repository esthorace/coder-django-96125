from django.contrib.auth.decorators import login_not_required  # type:ignore
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models.query import QuerySet
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from core.forms import CustomUserCreationForm, UserProfileForm


def saludar(request):
    return HttpResponse("Hola desde Django!")


def saludar2(request):
    return HttpResponse("<h1> Este es el título de la App </h1>")


def saludar3(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")


def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1, 6)

    if tiro_de_dado == 6:
        mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😊 ✨ Ganaste ✨"
    else:
        mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😒 Sigue intentando. Presiona F5"

    datos = {
        "titulo": "Tiro de Dados",
        "mensaje": mensaje,
        "fecha": datetime.now().strftime("%H:%M:%S.%f"),
    }
    return render(request, "core/dados.html", context=datos)


def ver_notas(request):
    lista_notas = [10, 8, 3, 7, 4, 5, 8]
    return render(request, "core/notas.html", {"notas": lista_notas})


def ver_usuarios(request):
    datos = [
        {"nombre": "juan", "email": "juan@django"},
        {"nombre": "santi", "email": "santi@django"},
        {"nombre": "agustín", "email": "agus@django"},
    ]
    return render(request, "core/usuarios.html", {"usuarios": datos})



@login_not_required
def index(request):
    ahora = datetime.now()
    contexto = {"fecha": ahora}
    return render(request, "core/index.html", contexto)


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")


class Profile(UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = "core/profile.html"
    success_url = reverse_lazy("core:index")

    def get_object(self):
        # UpdateView devuelve un pk o slug, pero debo devolver el usuario actual
        return self.request.user
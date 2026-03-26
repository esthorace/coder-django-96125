from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


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


def index(request):
    ahora = datetime.now()
    contexto = {"fecha": ahora}
    return render(request, "core/index.html", contexto)

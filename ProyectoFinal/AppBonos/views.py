from django.http import HttpResponse
from django.shortcuts import render
from AppBonos.models import Dolar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Agregado para avatar
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse

from AppBonos.forms import UserRegisterForm, UserEditionForm

from AppBonos.models import Avatar

from AppBonos.forms import AvatarForm, UserEditionForm


# Create your views here.

def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except:
        avatar = None
    return render(request, "AppBonos/padre.html", {"avatar": avatar})


@login_required
def about(request):
    return render(request, "AppBonos/about.html")


@login_required
def dolares(request):
    dolares = Dolar.objects.all()
    contexto = {"dolares_encontrados": dolares}
    return render(request, "AppBonos/dolares.html", context=contexto)


@login_required
def formularios(request):
    return render(request, "AppBonos/formularios.html")


@login_required
def procesar_form_dolares(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_dolares.html")

    dolar = Dolar(
        codigo=request.POST["codigo"],
        denominacion=request.POST["denominacion"],
        emisor=request.POST["emisor"],
        fecha_emision=request.POST["fecha_emision"],
        fecha_vencimiento=request.POST["fecha_vencimiento"],
        amortizacion=request.POST["amortizacion"],
        interes=request.POST["interes"],
        ley=request.POST["ley"],
    )

    dolar.save()
    return dolares(request)


@login_required
def busqueda(request):
    return render(request, "AppBonos/busqueda.html")


@login_required
def buscar(request):
    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        dolares = Dolar.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "dolares_encontrados": dolares}

        return render(request, "AppBonos/resultado_busqueda.html", contexto)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(
                    request,
                    "AppBonos/inicio.html",
                )
            else:
                return render(
                    request,
                    "AppBonos/login_error.html",
                    {"mensaje": "Datos Incorrectos. Intente nuevamente."},
                )

        else:
            return render(
                request,
                "AppBonos/login_error.html",
                {"mensaje": "Datos Incorrectos. Intente nuevamente."},
            )

    form = AuthenticationForm()

    return render(request, "AppBonos/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "AppBonos/registro_ok.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserRegisterForm()

    return render(request, "AppBonos/registro.html", {"form": form})



class DolarDelete(LoginRequiredMixin, DeleteView):

    model = Dolar
    success_url = "/AppBonos/dolares"



# Detail Views

class DolarDetail(LoginRequiredMixin, DetailView):

    model = Dolar
    template_name = "AppBonos/dolar_detalle.html"



# Update view

class DolarUpdateView(LoginRequiredMixin, UpdateView):
    model = Dolar
    fields = ["codigo", "denominacion", "emisor", "amortizacion", "interes", "ley"]

    def get_success_url(self):
        return reverse("dolares")





# Editar Perfil

@login_required
def editar_perfil(request):
    user = request.user

    if request.method == "POST":
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.password1 = data["password1"]
            user.password2 = data["password2"]
            user.save()

            return render(
                request,
                "AppBonos/editarPerfil_ok.html",
                {"mensaje": f"Usuario: {user.username}"},
            )

    else:
        form = UserEditionForm(
            initial={
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        )

    contexto = {"user": user, "form": form}
    return render(request, "AppBonos/editarPerfil.html", contexto)





# Avatar

@login_required
def agregar_avatar(request):
    user = request.user

    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return inicio(request)

    contexto = {"form": form}
    return render(request, "AppBonos/avatar_form.html", contexto)
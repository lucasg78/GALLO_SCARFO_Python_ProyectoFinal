from django.http import HttpResponse
from django.shortcuts import render
from AppBonos.models import Dolar, Peso, Pesobd, Pesodl, Especie
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic import (
    UpdateView,
    DeleteView,
)

from django.views.generic.detail import DetailView
from django.urls import reverse

from AppBonos.forms import UserRegisterForm, UserEditionForm

from AppBonos.models import Avatar

from AppBonos.forms import AvatarForm, UserEditionForm


# Sign in
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


# Sing up
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


# Inicio
def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except:
        avatar = None
    return render(request, "AppBonos/base.html", {"avatar": avatar})


# About
@login_required
def about(request):
    return render(request, "AppBonos/about.html")


# Dólares
@login_required
def dolares(request):
    dolares = Dolar.objects.all()
    contexto = {"dolares_encontrados": dolares}
    return render(request, "AppBonos/dolares.html", context=contexto)


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


    especie=Especie(
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
    especie.save()
    return dolares(request)


# Pesos (CER)
@login_required
def pesos(request):
    pesos = Peso.objects.all()
    contexto = {"pesos_encontrados": pesos}
    return render(request, "AppBonos/pesos.html", context=contexto)


@login_required
def procesar_form_pesos(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_pesos.html")

    peso = Peso(
        codigo=request.POST["codigo"],
        denominacion=request.POST["denominacion"],
        emisor=request.POST["emisor"],
        fecha_emision=request.POST["fecha_emision"],
        fecha_vencimiento=request.POST["fecha_vencimiento"],
        amortizacion=request.POST["amortizacion"],
        interes=request.POST["interes"],
        ley=request.POST["ley"],
    )

    especie=Especie(
        codigo=request.POST["codigo"],
        denominacion=request.POST["denominacion"],
        emisor=request.POST["emisor"],
        fecha_emision=request.POST["fecha_emision"],
        fecha_vencimiento=request.POST["fecha_vencimiento"],
        amortizacion=request.POST["amortizacion"],
        interes=request.POST["interes"],
        ley=request.POST["ley"],
    )

    peso.save()
    especie.save()
    return pesos(request)


# Pesos (BADLAR)
@ login_required
def pesosbd(request):
    pesosbd=Pesobd.objects.all()
    contexto={"pesosbd_encontrados": pesosbd}
    return render(request, "AppBonos/pesosbd.html", context=contexto)

@ login_required
def procesar_form_pesosbd(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_pesosbd.html")

    pesobd=Pesobd(
        codigo=request.POST["codigo"],
        denominacion=request.POST["denominacion"],
        emisor=request.POST["emisor"],
        fecha_emision=request.POST["fecha_emision"],
        fecha_vencimiento=request.POST["fecha_vencimiento"],
        amortizacion=request.POST["amortizacion"],
        interes=request.POST["interes"],
        ley=request.POST["ley"],
    )

    especie=Especie(
        codigo=request.POST["codigo"],
        denominacion=request.POST["denominacion"],
        emisor=request.POST["emisor"],
        fecha_emision=request.POST["fecha_emision"],
        fecha_vencimiento=request.POST["fecha_vencimiento"],
        amortizacion=request.POST["amortizacion"],
        interes=request.POST["interes"],
        ley=request.POST["ley"],
    )

    pesobd.save()
    especie.save()
    return pesosbd(request)



# Pesos (DL)
@ login_required
def pesosdl(request):
    pesosdl=Pesodl.objects.all()
    contexto={"pesosdl_encontrados": pesosdl}
    return render(request, "AppBonos/pesosdl.html", context=contexto)

@ login_required
def procesar_form_pesosdl(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_pesosdl.html")

    pesodl=Pesodl(
        codigo=request.POST["codigo"],
        denominacion=request.POST["denominacion"],
        emisor=request.POST["emisor"],
        fecha_emision=request.POST["fecha_emision"],
        fecha_vencimiento=request.POST["fecha_vencimiento"],
        amortizacion=request.POST["amortizacion"],
        interes=request.POST["interes"],
        ley=request.POST["ley"],
    )
    
    especie=Especie(
        codigo=request.POST["codigo"],
        denominacion=request.POST["denominacion"],
        emisor=request.POST["emisor"],
        fecha_emision=request.POST["fecha_emision"],
        fecha_vencimiento=request.POST["fecha_vencimiento"],
        amortizacion=request.POST["amortizacion"],
        interes=request.POST["interes"],
        ley=request.POST["ley"],
    )

    pesodl.save()
    especie.save()
    return pesosdl(request)



# Buscar
@ login_required
def busqueda(request):
    return render(request, "AppBonos/busqueda.html")

@ login_required
def buscar(request):
    if not request.GET["codigo"]:
        return HttpResponse("No enviaste ningún dato")
    else:
        codigo_a_buscar=request.GET["codigo"]
        especies=Especie.objects.filter(codigo=codigo_a_buscar)

        contexto={"codigo": codigo_a_buscar, "especies_encontrados": especies}

        return render(request, "AppBonos/resultado_busqueda.html", contexto)



# Views
# Dólares - Detalle
class DolarDetail(LoginRequiredMixin, DetailView):
    model=Dolar
    template_name="AppBonos/dolar_detalle.html"

# Dólares - Editar
class DolarUpdateView(LoginRequiredMixin, UpdateView):
    model=Dolar
    fields=["codigo", "denominacion", "emisor",
        "amortizacion", "interes", "ley"]
    def get_success_url(self):
        return reverse("dolares")

# Dólares - Borrar
class DolarDelete(LoginRequiredMixin, DeleteView):
    model=Dolar
    success_url="/AppBonos/dolares/"


# Pesos (CER) - Detalle
class PesoDetail(LoginRequiredMixin, DetailView):
    model=Peso
    template_name="AppBonos/peso_detalle.html"

# Pesos (CER) - Editar
class PesoUpdateView(LoginRequiredMixin, UpdateView):
    model=Peso
    fields=["codigo", "denominacion", "emisor",
        "amortizacion", "interes", "ley"]
    def get_success_url(self):
        return reverse("pesos")

# Pesos (CER) - Borrar
class PesoDelete(LoginRequiredMixin, DeleteView):
    model=Peso
    success_url="/AppBonos/pesosbd/"


# Pesos (BADLAR) - Detalle
class PesobdDetail(LoginRequiredMixin, DetailView):
    model=Pesobd
    template_name="AppBonos/pesobd_detalle.html"

# Pesos(BADLAR) - Editar
class PesobdUpdateView(LoginRequiredMixin, UpdateView):
    model=Pesobd
    fields=["codigo", "denominacion", "emisor",
        "amortizacion", "interes", "ley"]
    def get_success_url(self):
        return reverse("pesosbd")

# Pesos (BADLAR) - Borrar
class PesobdDelete(LoginRequiredMixin, DeleteView):
    model=Pesobd
    success_url="/AppBonos/pesosbd/"


# Pesos (DL) - Detalle
class PesodlDetail(LoginRequiredMixin, DetailView):
    model=Pesodl
    template_name="AppBonos/pesodl_detalle.html"

# Pesos(DL) - Editar
class PesodlUpdateView(LoginRequiredMixin, UpdateView):
    model=Pesodl
    fields=["codigo", "denominacion", "emisor",
        "amortizacion", "interes", "ley"]
    def get_success_url(self):
        return reverse("pesosdl")

# Pesos (DL) - Borrar
class PesodlDelete(LoginRequiredMixin, DeleteView):
    model=Pesodl
    success_url="/AppBonos/pesosdl/"



# Editar Perfil
@ login_required
def editar_perfil(request):
    user=request.user

    if request.method == "POST":
        form=UserEditionForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data

            user.first_name=data["first_name"]
            user.last_name=data["last_name"]
            user.email=data["email"]
            user.password1=data["password1"]
            user.password2=data["password2"]
            user.save()

            return render(
                request,
                "AppBonos/editarPerfil_ok.html",
                {"mensaje": f"Usuario: {user.username}"},
            )

    else:
        form=UserEditionForm(
            initial={
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        )

    contexto={"user": user, "form": form}
    return render(request, "AppBonos/editarPerfil.html", contexto)



# Avatar
@ login_required
def agregar_avatar(request):
    user=request.user

    if request.method != "POST":
        form=AvatarForm()
    else:
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u=User.objects.get(username=request.user)
            avatar=Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return inicio(request)

    contexto={"form": form}
    return render(request, "AppBonos/avatar_form.html", contexto)

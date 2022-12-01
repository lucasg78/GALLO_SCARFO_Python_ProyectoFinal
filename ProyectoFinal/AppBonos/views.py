from django.http import HttpResponse
from django.shortcuts import render
from AppBonos.models import Album, Dolar, Concierto, Articulo
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
def albums(request):
    albums = Album.objects.all()
    contexto = {"albums_encontrados": albums}
    return render(request, "AppBonos/albums.html", context=contexto)


@login_required
def conciertos(request):
    conciertos = Concierto.objects.all()
    contexto = {"conciertos_encontrados": conciertos}
    return render(request, "AppBonos/conciertos.html", context=contexto)


@login_required
def articulos(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos_encontrados": articulos}
    return render(request, "AppBonos/articulos.html", context=contexto)


@login_required
def formularios(request):
    return render(request, "AppBonos/formularios.html")


@login_required
def procesar_form_album(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_albums.html")

    album = Album(
        nombre=request.POST.get("nombreAlbum", "Temp"),
        cant_temas=request.POST.get("cantidadDeTemas", 10),
        fecha_de_lanzamiento=request.POST.get("fechaDeLanzamiento", "2020-10-20"),
    )

    album.save()
    return albums(request)


@login_required
def procesar_form_dolares(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_dolares.html")

    cantante = Dolar(
        nombre=request.POST["nombre"],
        apellido=request.POST["apellido"],
        fecha_nacimiento=request.POST["fecha_de_nacimiento"],
        email=request.POST["email"],
    )

    cantante.save()
    return dolares(request)


@login_required
def procesar_form_concierto(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_conciertos.html")

    concierto = Concierto(
        nombre=request.POST["nombre"],
        lugar=request.POST["lugar"],
        fecha_de_concierto=request.POST["fechaDelConcierto"],
    )

    concierto.save()
    return conciertos(request)


@login_required
def procesar_form_articulo(request):
    if request.method != "POST":
        return render(request, "AppBonos/form_articulos.html")

    articulo = Articulo(
        nombre=request.POST["nombre"],
        texto=request.POST["articulo"],
        fecha=request.POST["fechaDelArticulo"],
    )

    articulo.save()
    return articulos(request)


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


class AlbumDelete(LoginRequiredMixin, DeleteView):

    model = Album
    success_url = "/AppBonos/albums"


class ArticuloDelete(LoginRequiredMixin, DeleteView):

    model = Articulo
    success_url = "/AppBonos/articulos"


class CantanteDelete(LoginRequiredMixin, DeleteView):

    model = Dolar
    success_url = "/AppBonos/dolares"


class ConciertoDelete(LoginRequiredMixin, DeleteView):

    model = Concierto
    success_url = "/AppBonos/conciertos"


# Detail Views


class AlbumDetail(LoginRequiredMixin, DetailView):

    model = Album
    template_name = "AppBonos/album_detalle.html"


class ArticuloDetail(LoginRequiredMixin, DetailView):

    model = Articulo
    template_name = "AppBonos/articulo_detalle.html"


class CantanteDetail(LoginRequiredMixin, DetailView):

    model = Dolar
    template_name = "AppBonos/cantante_detalle.html"


class ConciertoDetail(LoginRequiredMixin, DetailView):

    model = Concierto
    template_name = "AppBonos/concierto_detalle.html"


# Update view


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ["nombre", "cant_temas", "fecha_de_lanzamiento"]

    def get_success_url(self):
        return reverse("albums")


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ["nombre", "texto", "fecha"]

    def get_success_url(self):
        return reverse("articulos")


class CantanteUpdateView(LoginRequiredMixin, UpdateView):
    model = Dolar
    fields = ["nombre", "apellido", "fecha_nacimiento", "email"]

    def get_success_url(self):
        return reverse("dolares")


class ConciertoUpdateView(LoginRequiredMixin, UpdateView):
    model = Concierto
    fields = ["nombre", "lugar", "fecha_de_concierto"]

    def get_success_url(self):
        return reverse("conciertos")


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
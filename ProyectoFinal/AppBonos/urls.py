from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from AppBonos.views import (
    DolarDetail,
    inicio,
    about,
    dolares,
    procesar_form_dolares,
    busqueda,
    buscar,
    formularios,
    login_request,
    register,
    editar_perfil,
    agregar_avatar,
)

from AppBonos.views import (
    DolarUpdateView,
)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("about/", about, name="about"),

    path("dolares/", dolares, name="dolares"),
    path("form_dolares/", procesar_form_dolares, name="form_dolares"),
    path("editar_dolar/<pk>", DolarUpdateView.as_view(), name="DolarUpdate"),
    path("detalle_dolar/<pk>", DolarDetail.as_view(), name="DolarDetail"),

    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
    path("formularios/", formularios, name="formularios"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="AppBonos/logout.html"), name="logout",),
    path("registro/", register, name="registro"),


    path("editar_perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar_avatar/", agregar_avatar, name="AgregarAvatar"),
]

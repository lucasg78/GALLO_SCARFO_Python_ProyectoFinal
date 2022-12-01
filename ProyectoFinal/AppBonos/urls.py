from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from AppBonos.views import (
    AlbumDelete,
    ArticuloDelete,
    CantanteDelete,
    ConciertoDelete,
    AlbumDetail,
    ArticuloDetail,
    CantanteDetail,
    ConciertoDetail,
    inicio,
    about,
    dolares,
    conciertos,
    albums,
    articulos,
    procesar_form_album,
    procesar_form_dolares,
    procesar_form_concierto,
    procesar_form_articulo,
    busqueda,
    buscar,
    formularios,
    login_request,
    register,
    editar_perfil,
    agregar_avatar,
)

from AppBonos.views import (
    AlbumUpdateView,
    ArticuloUpdateView,
    CantanteUpdateView,
    ConciertoUpdateView,
)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("about/", about, name="about"),
    path("dolares/", dolares, name="dolares"),
    path("conciertos/", conciertos, name="conciertos"),
    path("albums/", albums, name="albums"),
    path("articulos/", articulos, name="articulos"),
    path("form_albums/", procesar_form_album, name="form_albums"),
    path("form_dolares/", procesar_form_dolares, name="form_dolares"),
    path("form_conciertos/", procesar_form_concierto, name="form_conciertos"),
    path("form_articulos/", procesar_form_articulo, name="form_articulos"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
    path("formularios/", formularios, name="formularios"),
    path("login/", login_request, name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="AppBonos/logout.html"),
        name="logout",
    ),
    path("registro/", register, name="registro"),
    path("borrar_album/<pk>", AlbumDelete.as_view(), name="AlbumDelete"),
    path("borrar_articulo/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    path("borrar_cantante/<pk>", CantanteDelete.as_view(), name="CantanteDelete"),
    path("borrar_concierto/<pk>", ConciertoDelete.as_view(), name="ConciertoDelete"),
    path("detalle_album/<pk>", AlbumDetail.as_view(), name="AlbumDetail"),
    path("detalle_articulo/<pk>", ArticuloDetail.as_view(), name="ArticuloDetail"),
    path("detalle_cantante/<pk>", CantanteDetail.as_view(), name="CantanteDetail"),
    path("detalle_concierto/<pk>", ConciertoDetail.as_view(), name="ConciertoDetail"),
    path("editar_album/<pk>", AlbumUpdateView.as_view(), name="AlbumUpdate"),
    path("editar_cantante/<pk>", CantanteUpdateView.as_view(), name="CantanteUpdate"),
    path(
        "editar_concierto/<pk>", ConciertoUpdateView.as_view(), name="ConciertoUpdate"
    ),
    path("editar_articulo/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),
    path("editar_perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar_avatar/", agregar_avatar, name="AgregarAvatar"),
]

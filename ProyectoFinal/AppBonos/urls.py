from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from AppBonos.views import (
    DolarDetail,
    DolarDelete,
    PesoDetail,
    PesoDelete,
    PesobdDetail,
    PesobdDelete,
    inicio,
    about,
    dolares,
    procesar_form_dolares,
    pesos,
    procesar_form_pesos,
    pesosbd,
    procesar_form_pesosbd,
    busqueda,
    buscar,
    login_request,
    register,
    editar_perfil,
    agregar_avatar,
)

from AppBonos.views import (
    DolarUpdateView,
    PesoUpdateView,
    PesobdUpdateView,
)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("about/", about, name="about"),

    path("dolares/", dolares, name="dolares"),
    path("form_dolares/", procesar_form_dolares, name="form_dolares"),
    path("editar_dolar/<pk>", DolarUpdateView.as_view(), name="DolarUpdate"),
    path("detalle_dolar/<pk>", DolarDetail.as_view(), name="DolarDetail"),
    path("borrar_dolar/<pk>", DolarDelete.as_view(), name="DolarDelete"),

    path("pesos/", pesos, name="pesos"),
    path("form_pesos/", procesar_form_pesos, name="form_pesos"),
    path("editar_peso/<pk>", PesoUpdateView.as_view(), name="PesoUpdate"),
    path("detalle_peso/<pk>", PesoDetail.as_view(), name="PesoDetail"),
    path("borrar_peso/<pk>", PesoDelete.as_view(), name="PesoDelete"),

    path("pesosbd/", pesosbd, name="pesosbd"),
    path("form_pesosbd/", procesar_form_pesosbd, name="form_pesosbd"),
    path("editar_pesobd/<pk>", PesobdUpdateView.as_view(), name="PesobdUpdate"),
    path("detalle_pesobd/<pk>", PesobdDetail.as_view(), name="PesobdDetail"),
    path("borrar_pesobd/<pk>", PesobdDelete.as_view(), name="PesobdDelete"),

    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar, name="buscar"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="AppBonos/logout.html"), name="logout",),
    path("registro/", register, name="registro"),


    path("editar_perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar_avatar/", agregar_avatar, name="AgregarAvatar"),
]

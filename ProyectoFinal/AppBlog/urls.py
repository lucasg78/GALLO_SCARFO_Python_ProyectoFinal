from django.urls import path
from django.contrib.auth.views import *

from AppBlog.views import (
    MensajeUpdateView,
    MensajeDetail,
    MensajeDelete,
    blog,
    mensajes,
    procesar_form_mensajes,
)

urlpatterns = [
    path("blog/", blog, name="blog"),
    path("mensajes/", mensajes, name="mensajes"),
    path("form_mensajes/", procesar_form_mensajes, name="form_mensajes"),
    path("editar_mensaje/<pk>", MensajeUpdateView.as_view(), name="MensajeUpdate"),
    path("detalle_mensaje/<pk>", MensajeDetail.as_view(), name="MensajeDetail"),
    path("borrar_mensaje/<pk>", MensajeDelete.as_view(), name="MensajeDelete"),
]
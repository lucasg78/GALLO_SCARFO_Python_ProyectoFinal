from django.shortcuts import render
from AppBlog.models import Mensaje
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    UpdateView,
    DeleteView,
)

from django.views.generic.detail import DetailView
from django.urls import reverse



@login_required
def blog(request):
    return render(request, "AppBlog/base.html")


@login_required
def mensajes(request):
    mensajes = Mensaje.objects.all()
    contexto = {"mensajes_encontrados": mensajes}
    return render(request, "AppBlog/mensajes.html", context=contexto)


@login_required
def procesar_form_mensajes(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_mensajes.html")

    mensaje = Mensaje(
        nombre=request.POST["nombre"],
        email=request.POST["email"],
        mensaje=request.POST["mensaje"],
    )

    mensaje.save()
    return mensajes(request)


# Views
# Mensajes - Detalle
class MensajeDetail(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = "AppBlog/mensaje_detalle.html"

# Mensajes - Editar
class MensajeUpdateView(LoginRequiredMixin, UpdateView):
    model = Mensaje
    fields = ["nombre", "email", "mensaje"]
    def get_success_url(self):
        return reverse("mensajes")

# Mensajes - Borrar
class MensajeDelete(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = "/AppBlog/mensajes/"
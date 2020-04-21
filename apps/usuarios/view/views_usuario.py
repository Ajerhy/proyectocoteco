"""
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import (CreateView, UpdateView, DetailView, TemplateView, View, DeleteView,ListView)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.contrib import messages
from apps.usuarios.templatetags.utils import get_ip

import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from proyectocoteco import settings
from apps.usuarios.models import Usuario
#from apps.pacientes.models import Paciente,CentroSalud
from apps.usuarios.form.forms_usuario import UsuarioForm
from apps.usuarios.view.views_login import SinPrivilegios

USUARIO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Usuario'},
    {'string': 'Nombre'},
    {'string': 'Apellido'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]
""
usuarios|usuario|Can view usuario|usuarios.view_usuario
usuarios|usuario|Can add usuario|usuarios.add_usuario
usuarios|usuario|Can change usuario|usuarios.change_usuario
usuarios|usuario|Can delete usuario|usuarios.delete_usuario
""
#class UsuarioListarView(LoginRequiredMixin,ListView):
class UsuarioListarView(SinPrivilegios,TemplateView):
    #login_url = 'usuarios:index'
    permission_required = "usuarios.view_usuario"
    model = Usuario
    template_name = "geopuntospando/apps/usuarios/usuario/listar.html"

    def get_context_data(self, **kwargs):
        context = super(UsuarioListarView, self).get_context_data(**kwargs)
        usuariotodo = self.model.objects.all()
        usuarioactiva = self.model.objects.exclude(is_active='True')
        context['fields'] = USUARIO_FIELDS
        context["usuario_count"] = usuarioactiva
        context["list_usuario"] = usuariotodo
        return context

#Usuario Crear
class UsuarioCrearView(SuccessMessageMixin,SinPrivilegios,CreateView):
    #login_url = 'usuarios:index'
    permission_required = "usuarios.add_usuario"
    model = Usuario
    template_name = "geopuntospando/apps/usuarios/usuario/formulario.html"
    context_object_name = "obj_usuarios"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios:listar_usuario")
    success_message = "Usuario Creado Exitosamente"

#Usuario Actualizador
class UsuarioEditarView(SuccessMessageMixin,SinPrivilegios,UpdateView):
    #login_url = 'usuarios:index'
    permission_required = "usuarios.change_usuario"
    model = Usuario
    template_name = "geopuntospando/apps/usuarios/usuario/formulario.html"
    context_object_name = "obj_usuarios"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios:listar_usuario")
    success_message = "Usuario Actualizado Satisfactoriamente"

#Usuario Eliminar
class UsuarioEliminarView(SuccessMessageMixin, SinPrivilegios, DeleteView):
    #login_url = 'usuarios:index'
    permission_required = "usuarios.delete_usuario"
    model = Usuario
    template_name="geopuntospando/apps/usuarios/usuario/eliminar.html"
    success_url = reverse_lazy("usuarios:listar_usuario")
    success_message = "Usuario Eliminado Satisfactoriamente"

#Usuario Detalle
class UsuarioDetalleView(LoginRequiredMixin,DetailView):
    model = Usuario
    template_name = "geopuntospando/apps/usuarios/usuario/detalle.html"
    context_object_name = "obj"
    login_url = 'usuarios:index'

class ModalView(SinPrivilegios,ListView):
    model = Usuario
    template_name = "geopuntospando/apps/usuarios/usuario/modal.html"
    context_object_name = "obj"
    permission_required = "usuarios.view_usuario"
"""
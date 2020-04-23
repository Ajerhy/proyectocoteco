from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DetailView, TemplateView, View, DeleteView,ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import json
from apps.usuarios.templatetags.utils import get_ip
from django.db.models import Q

from apps.geolocalizacion.models import Localidad
from apps.geolocalizacion.forms.forms_localidad import LocalidadFrom

#class LocalidadListarView(LoginRequiredMixin,TemplateView):
class LocalidadListarView(LoginRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Localidad
    template_name = "pgcr/apps/geolocalizacion/localidad/listar.html"
    context_object_name = "list_localidad"

def cargar_localidades(request):
    municipios_id = request.GET.get('departamentos')
    #localidades = Localidad.objects.filter(municipios_id=municipios_id).order_by('nombrelocalidad')
    localidades = Localidad.objects.exclude(estado='False')
    return render(request, 'pgcr/apps/geolocalizacion/localidad/include/cargar_localidad.html',
                  {'localidades': localidades})









class LocalidadCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Localidad
    template_name = "geopuntospando/apps/geolocalizacion/localidad/formulario.html"
    context_object_name = "obj_localidad"
    form_class = LocalidadFrom
    success_url = reverse_lazy("geolocalizacion:listar_localidad")
    success_message = "Localidad Creada Exitosamente"

    def form_valid(self, form):
        localidad = form.save(commit=False)
        localidad.uc = self.request.user.id
        localidad.direccion_ip=get_ip(self.request)
        localidad.save()
        return super().form_valid(form)

class LocalidadEditarView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    login_url = 'usuarios:index'
    model = Localidad
    template_name = "geopuntospando/apps/geolocalizacion/localidad/formulario.html"
    context_object_name = "obj_localidad"
    form_class = LocalidadFrom
    success_url = reverse_lazy("geolocalizacion:listar_localidad")
    success_message = "Localidad Actualizado Satisfactoriamente"

    def form_valid(self, form):
        localidad = form.save(commit=False)
        localidad.um = self.request.user.id
        localidad.direccion_ip=get_ip(self.request)
        localidad.save()
        return super().form_valid(form)

class LocalidadDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Localidad
    template_name = 'geopuntospando/apps/geolocalizacion/localidad/detalle.html'#url
    context_object_name = 'obj'

class LocalidadEliminarView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Localidad
    template_name= 'geopuntospando/apps/geolocalizacion/localidad/eliminar.html'
    context_object_name='obj_provincia'
    success_url = reverse_lazy("geolocalizacion:listar_localidad")
    success_message="Localidad Eliminado Exitosamente"

@login_required(login_url='usuarios:index')
def cambiar_estado_localidad(request, pk):
    localidad = get_object_or_404(Localidad, pk=pk)
    if localidad.estado:
        localidad.estado = False
        messages.error(request, "Localidad Desactivada")
    else:
        localidad.estado = True
        messages.success(request, "Localidad Activada")
    localidad.um = request.user.id
    localidad.save()
    return redirect('geolocalizacion:listar_localidad')


@login_required(login_url='usuarios:index')
def localidaddesactivar(request, id):
    localidad = Localidad.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/localidad/estado_desactivar.html'#url

    if not localidad:
        return redirect('geolocalizacion:listar_localidad')

    if request.method=='GET':
        contexto={'obj':localidad}

    if request.method=='POST':
        localidad.estado=False
        localidad.um = request.user.id
        localidad.save()
        messages.error(request, "Localidad Desactivado")
        return redirect('geolocalizacion:listar_localidad')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def localidadactivar(request, id):
    localidad = Localidad.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/localidad/estado_activar.html'#url

    if not localidad:
        return redirect('geolocalizacion:listar_localidad')

    if request.method=='GET':
        contexto={'obj':localidad}

    if request.method=='POST':
        localidad.estado=True
        localidad.um = request.user.id
        localidad.save()
        messages.success(request, "Localidad Activado")
        return redirect('geolocalizacion:listar_localidad')

    return render(request,template_name,contexto)
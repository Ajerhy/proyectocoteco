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

from apps.geolocalizacion.models import Municipios,Departamentos,Provincias
from apps.geolocalizacion.forms.forms_municipios import MunicipiosForm

#class MunicipioListarView(LoginRequiredMixin,TemplateView):
class MunicipioListarView(LoginRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Municipios
    template_name = "pgcr/apps/geolocalizacion/municipio/listar.html"
    context_object_name = "list_municipio"

class MunicipioCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Municipios
    template_name = "pgcr/apps/geolocalizacion/municipio/form.html"
    context_object_name = "obj_municipio"
    form_class = MunicipiosForm
    success_url = reverse_lazy("geolocalizacion:listar_municipio")
    success_message = "Municipio Creado Exitosamente"

    def form_valid(self, form):
        municipio = form.save(commit=False)
        municipio.uc = self.request.user.id
        municipio.direccion_ip=get_ip(self.request)
        municipio.save()
        return super().form_valid(form)

class MunicipioEditarView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    login_url = 'usuarios:index'
    model = Municipios
    template_name = "pgcr/apps/geolocalizacion/municipio/form.html"
    context_object_name = "obj_municipio"
    form_class = MunicipiosForm
    success_url = reverse_lazy("geolocalizacion:listar_municipio")
    success_message = "Municipio Actualizado Satisfactoriamente"

    def form_valid(self, form):
        municipio = form.save(commit=False)
        municipio.um = self.request.user.id
        municipio.direccion_ip=get_ip(self.request)
        municipio.save()
        return super().form_valid(form)

class MunicipioDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Municipios
    template_name = 'pgcr/apps/geolocalizacion/municipio/detalle.html'#url
    context_object_name = 'obj'

class MunicipioEliminarView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Municipios
    template_name= 'pgcr/apps/geolocalizacion/municipio/eliminar.html'
    context_object_name='obj_municipio'
    success_url = reverse_lazy("geolocalizacion:listar_municipio")
    success_message="Municipio Eliminado Exitosamente"

@login_required(login_url='usuarios:index')
def municipiodesactivar(request, id):
    municipio = Municipios.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/municipio/estado_desactivar.html'#url

    if not municipio:
        return redirect('geolocalizacion:listar_municipio')

    if request.method=='GET':
        contexto={'obj':municipio}

    if request.method=='POST':
        municipio.estado=False
        municipio.um = request.user.id
        municipio.save()
        messages.error(request, "Municipio Desactivado")
        return redirect('geolocalizacion:listar_municipio')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def municipioactivar(request, id):
    municipio = Municipios.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/municipio/estado_activar.html'#url

    if not municipio:
        return redirect('geolocalizacion:listar_municipio')

    if request.method=='GET':
        contexto={'obj':municipio}

    if request.method=='POST':
        municipio.estado=True
        municipio.um = request.user.id
        municipio.save()
        messages.success(request, "Municipio Activado")
        return redirect('geolocalizacion:listar_municipio')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def cambiar_estado_municipio(request, pk):
    municipio = get_object_or_404(Municipios, pk=pk)
    if municipio.estado:
        municipio.estado = False
        messages.error(request, "Municipio Desactivada")
    else:
        municipio.estado = True
        messages.success(request, "Municipio Activada")
    municipio.um = request.user.id
    municipio.save()
    return redirect('geolocalizacion:listar_municipio')

def cargar_municipios(request):
    provincias_id = request.GET.get('provincias')
    #municipios = Municipios.objects.filter(provincias_id=provincias_id).order_by('nombremunicipios')
    municipios = Municipios.objects.exclude(estado='False')
    return render(request, 'pgcr/apps/geolocalizacion/municipio/include/cargar_municipios.html',
                  {'municipios': municipios})


#class MunicipioDependienteView(LoginRequiredMixin,ListView):
class MunicipioDependienteView(LoginRequiredMixin,TemplateView):
    login_url = 'usuarios:index'
    model = Municipios
    template_name = "pgcr/apps/geolocalizacion/municipio/dependiente.html"

    def get_context_data(self, **kwargs):
        context = super(MunicipioDependienteView, self).get_context_data(**kwargs)
        context["departamentos"] = Departamentos.objects.exclude(estado='False')
        context["provincias"] = Provincias.objects.exclude(estado='False')
        return context
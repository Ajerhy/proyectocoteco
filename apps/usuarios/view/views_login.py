from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (TemplateView, View)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth import update_session_auth_hash

#from apps.usuarios.models import Usuario
#from apps.pacientes.models import Paciente,CentroSalud,Casos
#from apps.usuarios.form.forms_usuario import LoginUsuarioForm

class Index(TemplateView):
    template_name="coteco/apps/index.html"

class Login(TemplateView):
    template_name="coteco/apps/usuarios/login.html"

class Registrar(TemplateView):
    template_name="coteco/apps/usuarios/registrar.html"

class Perfil(TemplateView):
    template_name="coteco/apps/usuarios/perfil.html"

class Error404(TemplateView):
    template_name="coteco/apps/usuarios/404.html"

class Categoria(TemplateView):
    template_name= "coteco/apps/categorias/categoria.html"

class DetalleCategoria(TemplateView):
    template_name= "coteco/apps/categorias/detalle.html"

class Paquete(TemplateView):
    template_name= "coteco/apps/paquetes/paquete.html"

class Informacion(TemplateView):
    template_name= "coteco/apps/informacion/informacion.html"

class Contactanos(TemplateView):
    template_name= "coteco/apps/informacion/contactame.html"

class Blog(TemplateView):
    template_name= "coteco/apps/blogs/blog.html"

class BlogUnico(TemplateView):
    template_name= "coteco/apps/blogs_unico/blog_unico.html"

class Anuncio(TemplateView):
    template_name= "coteco/apps/anuncios/anuncio.html"

class ListadoAnuncio(TemplateView):
    template_name= "coteco/apps/anuncios/listado_anuncio.html"

class Tienda(TemplateView):
    template_name= "coteco/apps/tiendas/tienda.html"

class Termino(TemplateView):
    template_name= "coteco/apps/termino_condicion/termino_condicion.html"

"""
class SinPrivilegios(LoginRequiredMixin,PermissionRequiredMixin):
    login_url = 'usuarios:indeX'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='usuarios:sinprivilegio'
        return HttpResponseRedirect(reverse_lazy(self.login_url))
"""
"""
class SinPrivilegios(PermissionRequiredMixin):
    login_url = 'usuarios:sinprivilegio'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy(self.login_url))
"""
"""
class DashboardSinPrivilegio(LoginRequiredMixin, TemplateView):
    login_url = 'usuarios:index'
    template_name="geopuntospando/apps/usuarios/permiso/privilegio.html"

#Ordenar(Template despues LoginRequiredMixin)
# permission_required = "usuarios.view_usuario"
class LoginView(TemplateView,LoginRequiredMixin):
    login_url = 'usuarios:index'
    template_name = "geopuntospando/apps/usuarios/index.html"#url
    success_url = reverse_lazy("usuarios:dashboard")#url

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LoginUsuarioForm(request.POST, request=request)
        if form.is_valid():
            user = Usuario.objects.filter(usuario=request.POST.get('usuario')).first()
            if user is not None:
                if user.is_active:
                    user = authenticate(
                        usuario=request.POST.get('usuario'),
                        password=request.POST.get('password'))
                    if user is not None:
                        login_django(request, user)
                        return redirect('usuarios:dashboard')
                    return render(request, self.template_name, {
                        "error": True,
                        "message": "Tu nombre de usuario y contraseña no coinciden. Inténtalo de nuevo."}
                                  )
                return render(request, self.template_name, {
                    "error": True,
                    "message": "Su cuenta está inactiva. Por favor, póngase en contacto con el administrador"}
                              )
            return render(request, self.template_name, {
                "error": True,
                "message": "Tu cuenta no se encuentra. Por favor, póngase en contacto con el administrador"}
                          )
        return render(request, self.template_name, {
            # "error": True,
            # "message": "Tu nombre de Usuario y Contraseña no coinciden. Inténtalo de nuevo."
            "form": form
        })

#permission_required = "usuarios.view_usuario"
class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'geopuntospando/apps/dashboard.html'
    login_url = 'usuarios:index'
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['usuario'] = self.model.objects.exclude(is_superuser=True)
        #context['pacientes_activo'] = Paciente.objects.exclude(estado='False')
        context['casos'] = Casos.objects.get(id=1)
        #context['casos'] = Casos.objects.all('sospechoso','porcentaje')
        #context['casos'] = Casos.objects.values('sospechoso','porcentaje')
        context['pacientes'] = Paciente.objects.all()
        context['centrosalud_list'] = CentroSalud.objects.all()
        return context

#Salir
@login_required(login_url='usuarios:index')
def LogoutView(request):
    logout_django(request)
    return redirect('usuarios:index')

def handler400(request,exception=None):
    return render(request, 'geopuntospando/apps/usuarios/permiso/400.html', status=400)

def handler403(request,exception=None):
    return render(request, 'geopuntospando/apps/usuarios/permiso/403.html', status=403)

def handler404(request,exception):
    return render(request, 'geopuntospando/apps/usuarios/permiso/404.html', status=404)

def handler500(request,exception=None):
    return render(request, 'geopuntospando/apps/usuarios/permiso/500.html', status=500)
"""
"""
def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response
"""
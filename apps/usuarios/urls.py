from django.urls import path

from apps.usuarios.view.views_login import Error404,Login,Registrar,Perfil,Index,Categoria,DetalleCategoria,Paquete,Informacion,Contactanos,Blog,BlogUnico,Anuncio,ListadoAnuncio,Tienda,Termino
#    LoginView,DashboardView,LogoutView,DashboardSinPrivilegio,\

    #,e404,e500

#from apps.usuarios.view.views_usuario import UsuarioListarView,UsuarioCrearView,\
#    UsuarioEditarView,UsuarioEliminarView,UsuarioDetalleView,ModalView

#from apps.usuarios.view.views_perfil import PerfilListarView

app_name = 'usuarios'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('registrar/', Registrar.as_view(), name='registrar'),
    path('perfil/', Perfil.as_view(), name='perfil'),
    path('404/', Error404.as_view(), name='404'),

    path('categoria/', Categoria.as_view(), name='categoria'),
    path('detalle/categoria/', DetalleCategoria.as_view(), name='categoria_detalle'),

    path('paquete/', Paquete.as_view(), name='paquete'),
    path('sobre/nosotros/', Informacion.as_view(), name='informacion'),
    path('contactanos/', Contactanos.as_view(), name='contactame'),
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/unico/', BlogUnico.as_view(), name='blog_unico'),
    path('dasboard/', Anuncio.as_view(), name='anuncio'),
    path('listar/anuncio/', ListadoAnuncio.as_view(), name='listar_anuncio'),

    path('tienda/', Tienda.as_view(), name='tienda'),
    path('terminos/condiciones/', Termino.as_view(), name='termino'),


]
# Inicio
"""
path('', LoginView.as_view(), name='index'),
path('dashboard/', DashboardView.as_view(), name='dashboard'),
path('logout/', LogoutView, name='logout'),
path('sin/privilegio/',DashboardSinPrivilegio.as_view(),name='sinprivilegio'),

#path('error/404/', e404, name='404'),
#path('error/500/', e500, name='500'),

#Usuario
path('usuario/listar/', UsuarioListarView.as_view(), name='listar_usuario'),
path('usuario/crear/', UsuarioCrearView.as_view(), name='crear_usuario'),
path('usuario/<int:pk>/editar/', UsuarioEditarView.as_view(), name="editar_usuario"),
path('usuario/<int:pk>/eliminar/', UsuarioEliminarView.as_view(), name="eliminar_usuario"),
path('usuario/<int:pk>/detalle/', UsuarioDetalleView.as_view(), name='detalle_usuario'),
path('modal/', ModalView.as_view(), name='modal_usuario'),
"""
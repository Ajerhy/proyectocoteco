from django.db import models
from django.urls import reverse
import uuid
from apps.usuarios.models import EstadoModelo

class SitioWebConfiguracion(EstadoModelo):
    ver_blog = models.BooleanField('Mostrar Blog', default=False)
    ver_servicio = models.BooleanField('Mostrar Servicios', default=False)
    ver_anuncio = models.BooleanField('Mostrar Anuncios', default=False)
    ver_tienda = models.BooleanField('Mostrar Tienda', default=False)
    ver_construccion = models.BooleanField('En Construcción', default=False)

    def __str__(self):
        return "%s" % (self.id)

    def get_absolute_url(self):
        return reverse('sitioweb-configuracion', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-creacion']
        verbose_name_plural = "Sitio Web Configuracion"

class Blog(EstadoModelo):
    titulo = models.CharField('Titulo', max_length=255)
    contenido = models.TextField()

    def get_absolute_url(self):
        return reverse('blog-detalle', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.titulo)

    class Meta:
        ordering = ['-creacion']
        verbose_name_plural = "Blogs"

#
class Trabajo(EstadoModelo):
    nombretrabajo = models.CharField(max_length=50, blank=False, null=False)
    preciotrabajo = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "Trabajos"
        ordering = ['-creacion']
#
class Servicio(EstadoModelo):
    codigoservicio = models.UUIDField('codigoservicio', default=uuid.uuid4, unique=True, null=False, blank=False, editable=False)
    nombreservicio = models.CharField(max_length=50, blank=False, null=False,verbose_name='Nombre del Servicio',
                                            help_text='Ingrese Nombre del Servicio')
    siglaservicio = models.CharField(max_length=20, blank=True, null=True,
                                            verbose_name='Sigla del Servicio',
                                            help_text='Ingrese la Sigla del Servicio')
    descripcionservicio = models.CharField(max_length=50, blank=True, null=True,
                                            verbose_name='Descripcion del Servicio',
                                            help_text='Ingrese Descripcion del Servicio')
    icono = models.CharField(max_length=20, blank=True, null=True,
                                     verbose_name='Icono del Servicio',
                                     help_text='Ingrese Icono del Servicio')

    def __str__(self):
        return "%s" % (self.nombreservicio)

    def get_absolute_url(self):
        return reverse('servicio-detalle', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Servicios"
        ordering = ['-creacion']

class Anuncio(EstadoModelo):
    codigoanuncio = models.UUIDField('codigoanuncio', default=uuid.uuid4, unique=True, null=False, blank=False, editable=False)
    nombranuncio = models.CharField(max_length=50, blank=False, null=False,verbose_name='Nombre del Anuncio',
                                            help_text='Ingrese Nombre del Anuncio')
    descripcionanuncio = models.CharField(max_length=50, blank=True, null=True,
                                            verbose_name='Descripcion del Anuncio',
                                            help_text='Ingrese Descripcion del Anuncio')
    icono = models.CharField(max_length=20, blank=True, null=True,
                                     verbose_name='Icono del Anuncio',
                                     help_text='Ingrese Icono del Anuncio')

    def __str__(self):
        return "%s" % (self.nombranuncio)

    def get_absolute_url(self):
        return reverse('anuncio-detalle', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Anuncios"
        ordering = ['-creacion']

class Tienda(EstadoModelo):
    nombre = models.CharField('nombre', max_length=255)
    contenido = models.TextField()

    def get_absolute_url(self):
        return reverse('tienda-detalle', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.nombre)

    class Meta:
        ordering = ['-creacion']
        verbose_name_plural = "Tiendas"
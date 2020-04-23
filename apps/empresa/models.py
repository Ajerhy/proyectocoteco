import binascii
import os
from django.db import models
from django.urls import reverse
from apps.usuarios.models import EstadoModelo
from apps.geolocalizacion.models import Departamentos,Provincias,Municipios,Localidad,Direccion

class ReferenciaMovil(EstadoModelo):
    telefonomovil = models.CharField(max_length=50, blank=True, null=True,
                                    verbose_name='Numero Telefonico',
                                    help_text='Ingrese Numero Telefonico')

    def get_absolute_url(self):
        return reverse('referenciamovil-detalle', kwargs={'pk': self.pk})

    def __str__(self):
        return (self.telefonomovil)

    class Meta:
        verbose_name_plural = "Referencia Telefonica"
        ordering = ['creacion']

class Emprendimiento(EstadoModelo):
    nombre = models.CharField(max_length=40)
    telefono = models.ManyToManyField(ReferenciaMovil, blank=True)
    email = models.EmailField(max_length=40, blank=True)
    giro = models.CharField(max_length=80, blank=True)

    departamento = models.ForeignKey(Departamentos, null=True, blank=True, on_delete=models.CASCADE)
    privincia = models.ForeignKey(Provincias, null=True, blank=True, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipios, null=True, blank=True, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='static/photos/', null=True, blank=True)#faltacorregir
    icono = models.CharField(max_length=20, blank=True, null=True,verbose_name='Icono del Emprendimiento',
                                         help_text='Ingrese Icono del Emprendimiento')

    mision = models.TextField(blank=True, null=True,verbose_name='Mision de la Emprendimiento',
                                 help_text='Ingrese la Mision de la Emprendimiento')
    vision = models.TextField(blank=True, null=True,verbose_name='Vision de la Emprendimiento',
                                 help_text='Ingrese la Vision de la Emprendimiento')
    slogan = models.CharField('Eslogan', max_length=250, blank=True)
    terminos = models.TextField(blank=True, null=True)
    condiciones = models.TextField(blank=True, null=True)

    social_youtube = models.CharField(max_length=255, blank=True)
    social_facebook = models.CharField(max_length=255, blank=True)
    social_instagram = models.CharField(max_length=255, blank=True)
    social_tiktok = models.CharField(max_length=255, blank=True)
    social_twitter = models.CharField(max_length=255, blank=True)
    social_snapchat = models.CharField(max_length=255, blank=True)
    social_linkedin = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('emprendimiento-detalle', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.nombre)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Emprendimiento"
        ordering = ['-creacion']

def generate_key():
    return binascii.hexlify(os.urandom(8)).decode()

class APIConfiguracion(EstadoModelo):
    titulo = models.CharField(max_length=1000)
    apikey = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=255, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.apikey or self.apikey is None or self.apikey == "":
            self.apikey = generate_key()
        super(APIConfiguracion, self).save(*args, **kwargs)

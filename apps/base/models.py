from django.db import models
from django.urls import reverse
from apps.usuarios.models import EstadoModelo
from apps.empresa.models import Emprendimiento

class BaseConfiguracion(EstadoModelo):
    enlinea = models.BooleanField('En linea', default=False)
    principal_emprendimiento = models.ForeignKey(Emprendimiento, on_delete='cascade', null=True, blank=True)
    menu_abierto = models.BooleanField('Menu Abierto', default=True)
    cargar_datos = models.BooleanField('Cargar Datos', default=False)

    def get_absolute_url(self):
        return reverse('base-configuracion', kwargs={'pk': self.pk})

    def dcargar_datos(self):
        self.cargar_datos = True

from django.contrib import admin
from apps.empresa.models import ReferenciaMovil,Emprendimiento,APIConfiguracion

admin.site.register(ReferenciaMovil)
admin.site.register(Emprendimiento)
admin.site.register(APIConfiguracion)
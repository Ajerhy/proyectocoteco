from django.views.generic.edit import UpdateView
from apps.base.models import BaseConfiguracion
from django.shortcuts import render


class UpdateBaseConfiguracionView(UpdateView):
    model = BaseConfiguracion
    template_name = 'erp/form.html'
    fields = ['enlinea', 'menu_abierto','principal_emprendimiento']


def LoadData(request):
    state = BaseConfiguracion.objects.get(pk=1).load_data
    if state:
        print("Ya existe Data")
    else:
        print("Cargamos")
    return render(request, 'base/ok.html')


#   enlinea principal_emprendimiento menu_abierto cargar_datos
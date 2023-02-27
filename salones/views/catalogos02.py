from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import loader
from django.shortcuts import  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .catalogos01 import *
from .eventos import *
from .personas import *
from .restview import * 
from .sistema import *

from salones.models import DesgloseServicio, ClasifServicio

####### Clasificacion Servicio #########

class desglose_servicio_lista(ListView):
    model = DesgloseServicio
    template_name  = 'salones/catalogos/list.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        lista = TipoPersona.objects.all().order_by('clave').values()
        datos = {
            'lista': lista,
            'titulo': "Desglose de Servicio",
            'add':"add_desglose_servicio",
            'add_label':'Nuevo desglose de servicio',
            'update':'update_desglose_servicio',  
            'detalle':'detalle_desglose_servicio',
            'borra':'borra_desglose_servicio',
            'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    


####### Desglose Servicio #########
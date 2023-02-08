from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.views import generic
from django.urls import reverse, reverse_lazy

from salones.models import (
    TipoActividad, 
    TipoEvento, 
    TipoServicio,
    TipoPersona, 
    Foto, 
    EncEvento,
    PersonaPrincipal,
)
from .forms import (
    ActividadForm, 
    EventoForm, 
    ServicioForm,
    EventoCompletoForm,
    PersonaPrincipalForm,
    TipoClienteForm,
    )


def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'salones/account.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'salones/login.html', {'error_message': 'Nombre o contraseña incorrecta.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'salones/login.html')

def home_view(request):   
    template = loader.get_template('home.html')
    fotos = Foto.objects.all()
    context = {'titulo': "Nueva Actividad", "fotos": fotos, 'regresa':'lista_actividad'}
    return HttpResponse(template.render(context, request))

#Catalogos

def add_actividad(request):
    form = ActividadForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect(lista_actividad)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nueva Actividad", "form": form, 'regresa':'lista_actividad'}
    return HttpResponse(template.render(context, request))

def update_actividad(request, id_actividad):
    actividad = get_object_or_404(TipoActividad, pk=id_actividad)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=actividad)
        if form.is_valid():
            form.save()
            return redirect(lista_actividad)
    else:
        form = EventoForm(instance=actividad)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': actividad, 'titulo': "Actualiza Actividad", "form": form, 'regresa':'lista_actividad'}
    return HttpResponse(template.render(context, request))

def lista_actividad(request):
    actividad_list = TipoActividad.objects.all().order_by('clave').values()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': actividad_list,
        'titulo': "Actividades",
        'add':"add_actividad",
        'add_label':'Nueva actividad',
        'update':'update_actividad',
        'detalle':'detalle_actividad',
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))


  
def add_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect(lista_evento)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Evento", "form": form, 'regresa':'lista_evento'}
    return HttpResponse(template.render(context, request))

class update_evento(generic.edit.UpdateView):
    model = TipoEvento
    fields = ['clave','descripcion','bandactivo']
    success_url = reverse_lazy('lista_evento')
    template_name = 'salones/catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Evento"
        context['regresa'] = 'lista_evento'
        return context


# def update_evento(request, id_evento):
#     evento = get_object_or_404(TipoEvento, pk=id_evento)
#     if request.method == 'POST':
#         form = EventoForm(request.POST,instance=evento)
#         if form.is_valid():
#             form.save()
#             return redirect(lista_evento)
#     else:
#         form = EventoForm(instance=evento)
#     template = loader.get_template('salones/catalogos/update.html')
#     context = {'catalogo': evento, 'titulo': "Actualiza Evento", "form": form, 'regresa':'lista_evento'}
#     return HttpResponse(template.render(context, request))


class lista_evento(generic.ListView):
    model = TipoEvento
    template_name = ('salones/catalogos/list.html')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lista'] = TipoEvento.objects.all().order_by('clave').values()
        datos = {
            'titulo': "Eventos",
            'add':"add_evento",
            'add_label':'Nuevo Evento',
            'update':'update_evento',        
            'detalle':'detalle_evento',
            'encabezados': {"id":'Folio',"clav e":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    


def add_servicio(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(lista_servicio)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Servicio", "form": form, 'regresa':'lista_servicio'}
    return HttpResponse(template.render(context, request))   

def update_servicio(request, id_servicio):
    servicio = get_object_or_404(TipoServicio, pk=id_servicio)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=servicio)
        if form.is_valid():
            form.save()
            return redirect(lista_servicio)
    else:
        form = ServicioForm(instance=servicio)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': servicio, 'titulo': "Actualiza Servicio", "form": form, 'regresa':'lista_servicio'}
    return HttpResponse(template.render(context, request))

def lista_servicio(request):
    servicio_list = TipoServicio.objects.all().order_by('clave').values()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': servicio_list,
        'titulo': "Servicios",
        'add':"add_servicio",
        'add_label':'Nuevo Servicio',
        'update':'update_servicio',
        'detalle':'detalle_servicio',
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))


from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ActividadSerializer, EventoSerializer, ServicioSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    queryset = TipoActividad.objects.all()
    serializer_class = ActividadSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventoViewSet(viewsets.ModelViewSet):
    queryset = TipoEvento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [permissions.IsAuthenticated]



class eventos(generic.ListView):
    model = EncEvento
    template_name = 'salones/list_evento.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        datos = {
                'titulo': "Eventos",
                'add':"add_evento_completo",
                'add_label':'Nuevo evento',
                'update':'update_evento_completo',
                'encabezados': {
                    "folioevento":'ID',
                    "evento":"CLAVE EVENTO",
                    "persona":"CLIENTE", 
                    "opcion":"OPCION",
                    "nombre":"NOMBRE",
                    "banaprovada":"ACTIVA",
                    },
            }
        context.update(datos)
        return context

def detail_evento(request, id_evento):    
    evento = get_object_or_404(EncEvento, pk=EncEvento)
    form = EventoCompletoForm(request.POST, instance=evento)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(eventos)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Evento", "form": form, 'regresa':'eventos'}
    return HttpResponse(template.render(context, request))
    

def add_evento_completo(request):
    form = EventoCompletoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.opcion = 1 #Agrega la opcion 1 a la instancia
        instance.save() 
        #return redirect(eventos)
        return  redirect(reverse('update_evento_completo', kwargs={'evento_id': instance.id}))   
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Evento", "form": form, 'regresa':'eventos'}
    return HttpResponse(template.render(context, request))

def update_evento_completo(request, id_evento):
    evento = get_object_or_404(EncEvento, pk=id_evento)
    if request.method == 'POST':
        form = EventoCompletoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect(eventos)
    else:
        form = EventoCompletoForm(instance=evento)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': evento, 'titulo': "Actualiza Evento", "form": form, 'regresa':'eventos'}
    return HttpResponse(template.render(context, request))



def detalle_actividad(request, id_ctividad):
    evento = get_object_or_404(TipoActividad, pk=id_ctividad)
    if request.method == 'POST':
        form = ActividadForm(request.POST,instance=evento)
        if form.is_valid():
            form.save()
            return redirect(lista_actividad)
    else:
        form = ActividadForm(instance=evento)
    template = loader.get_template('salones/catalogos/detalle.html')
    context = {'catalogo': evento, 'titulo': "Detalle actividad", "form": form, 'regresa':'lista_evento'}
    return HttpResponse(template.render(context, request))

def detalle_evento(request, id_evento):
    evento = get_object_or_404(TipoEvento, pk=id_evento)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=evento)
        if form.is_valid():
            form.save()
            return redirect(lista_evento)
    else:
        form = EventoForm(instance=evento)
    template = loader.get_template('salones/catalogos/detalle.html')
    context = {'catalogo': evento, 'titulo': "Detalle Evento", "form": form, 'regresa':'lista_evento'}
    return HttpResponse(template.render(context, request))
    
def detalle_servicio(request, id_servicio):
    servicio = get_object_or_404(TipoServicio, pk=id_servicio)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=servicio)
        if form.is_valid():
            form.save()
            return redirect(lista_evento)
    else:
        form = EventoForm(instance=servicio)
    template = loader.get_template('salones/catalogos/detalle.html')
    context = {'catalogo': servicio, 'titulo': "Detalle Servicio", "form": form, 'regresa':'lista_servicio'}
    return HttpResponse(template.render(context, request))


class personas(generic.ListView):
    model = PersonaPrincipal
    template_name  = 'salones/list_cliente.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lista'] = EncEvento.objects.all()

        datos = {
            'titulo': "Personas",
            'add':"add_cliente",
            'add_label':'Nueva Persona',
            'update':'update_cliente',
            'encabezados': {
                "id":"ID",
                "nombre":'NOMBRE',
                "primer_apellido":"PRIMER APELLIDO",
                "segundo_apellido":"SEGUNDO APELLIDO", 
                "cvetipopersona":"TIPO",
                "correo":"CORREO",
                },
        }
        context.update(datos)
        return context


def add_cliente(request):
    form = PersonaPrincipalForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(lista_servicio)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nueva Persona", "form": form, 'regresa':'clientes'}
    return HttpResponse(template.render(context, request))   

def update_cliente(request, id_persona):
    persona = get_object_or_404(PersonaPrincipal, pk=id_persona)
    if request.method == 'POST':
        form = PersonaPrincipalForm(request.POST,instance=persona)
        if form.is_valid():
            form.save()
            return redirect(lista_tipo_cliente)
    else:
        form = PersonaPrincipalForm(instance=persona)  
    template = loader.get_template('salones/catalogos/update.html')
    context = {"catalogo": persona,'titulo': "Actualiza persona", "form": form, 'regresa':'clientes'}
    return HttpResponse(template.render(context, request))   

class lista_tipo_persona(generic.ListView):
    model = TipoPersona
    template_name  = 'salones/catalogos/list.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        lista = TipoPersona.objects.all().order_by('clave').values()
        datos = {
            'lista': lista,
            'titulo': "Tipo Persona",
            'add':"add_tipo_cliente",
            'add_label':'Nuevo Tipo Persona',
            'update':'update_tipo_cliente',  
            'detalle':'detalle_servicio',
            'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    

def lista_tipo_cliente(request):
    clientes = TipoPersona.objects.all().values()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': clientes,
        'titulo': "Tipo Persona",
        'add':"add_tipo_cliente",
        'add_label':'Nuevo Tipo Persona',
        'update':'update_tipo_cliente',  
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))


def add_tipo_cliente(request):
    form = TipoClienteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect(lista_tipo_cliente)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Tipo Cliente", "form": form, 'regresa':'lista_tipo_cliente'}
    return HttpResponse(template.render(context, request))

def update_tipo_cliente(request, id_tipo_persona):
    tipo_persona = get_object_or_404(TipoPersona, pk=id_tipo_persona)
    if request.method == 'POST':
        form = TipoClienteForm(request.POST,instance=tipo_persona)
        if form.is_valid():
            form.save()
            return redirect(lista_tipo_cliente)
    else:
        form = TipoClienteForm(instance=tipo_persona)  
    template = loader.get_template('salones/catalogos/update.html')
    context = {"catalogo": tipo_persona, 'titulo': "Actualiza Tipo Cliente", "form": form, 'regresa':'lista_tipo_cliente'}
    return HttpResponse(template.render(context, request))

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
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
    EventoFormModal,
    EventoCompletoForm,
    PersonaPrincipalForm,
    TipoClienteForm,
    )

class ActividadCreateView(CreateView):
    model = TipoActividad
    fields = ('clave', 'descripcion')

class EventoCreateView(CreateView):
    model = TipoEvento
    fields = ('clave', 'descripcion')

class ServicioCreateView(CreateView):
    model = TipoServicio
    fields = ('clave', 'descripcion')

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

def add_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect(lista_evento)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Evento", "form": form, 'regresa':'lista_evento'}
    return HttpResponse(template.render(context, request))


def update_evento(request, id_evento):
    evento = get_object_or_404(TipoEvento, pk=id_evento)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=evento)
        if form.is_valid():
            form.save()
            return redirect(lista_evento)
    else:
        form = EventoForm(instance=evento)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': evento, 'titulo': "Actualiza Evento", "form": form, 'regresa':'lista_evento'}
    return HttpResponse(template.render(context, request))

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

def lista_evento(request):
    eventos_list = TipoEvento.objects.all().order_by('clave').values()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': eventos_list,
        'titulo': "Eventos",
        'add':"add_evento",
        'add_label':'Nuevo Evento',
        'update':'update_evento',        
        'detalle':'detalle_evento',
        'encabezados': {"id":'Folio',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
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


def eventos(request):
    actividad_list = EncEvento.objects.all().values()
    template = loader.get_template('salones/list_evento.html')
    context = {
        'lista': actividad_list,
        'titulo': "Eventos",
        'add':"add_evento_completo",
        'add_label':'Nuevo evento',
        'update':'update_evento_completo',
        'encabezados': {
            "folioevento":'ID',
            "cvetipoevento":"CLAVE EVENTO",
            "cvepersona":"CLIENTE", 
            "opcion":"OPCION",
            "nombre":"NOMBRE",
            "banaprovada":"ACTIVA",
            },
    }
    return HttpResponse(template.render(context, request))


def add_evento_completo(request):
    form = EventoCompletoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect(eventos)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Evento", "form": form, 'regresa':'eventos'}
    return HttpResponse(template.render(context, request))

def update_evento_completo(request, id_evento):
    evento = get_object_or_404(EventoCompletoForm, pk=id_evento)
    if request.method == 'POST':
        form = EventoCompletoForm(request.POST,instance=evento)
        if form.is_valid():
            form.save()
            return redirect(eventos)
    else:
        form = EventoCompletoForm(instance=evento)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': evento, 'titulo': "Actualiza Tipo Cliente", "form": form, 'regresa':'eventos'}
    return HttpResponse(template.render(context, request))



from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)
from django.urls import reverse_lazy

class EventoCreateView(BSModalCreateView):
    template_name = 'salones/catalogos/create.html'
    form_class = EventoFormModal
    success_message = 'Success: Se creo Evento'
    success_url = reverse_lazy('lista_evento')


class EventoUpdateView(BSModalUpdateView):
    model = TipoEvento
    template_name = 'examples/update_book.html'
    form_class = EventoFormModal
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('lista_evento')


class EventoReadView(BSModalReadView):
    model = TipoEvento
    template_name = 'salones/catalogos/detalle.html'


class EventoDeleteView(BSModalDeleteView):
    model = TipoEvento
    template_name = 'salones/catalogos/borrar.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('lista_evento')

def detalle_actividad(request, id_ctividad):
    evento = get_object_or_404(TipoActividad, pk=id_ctividad)
    if request.method == 'POST':
        form = ActividadForm(request.POST,instance=evento)
        if form.is_valid():
            form.save()
            return redirect(lista_evento)
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


def clientes(request):
    actividad_list = PersonaPrincipal.objects.all().values()
    template = loader.get_template('salones/list_evento.html')
    context = {
        'lista': [],
        'titulo': "Clientes",
        'add':"add_cliente",
        'add_label':'Nuevo Cliente',
        'update':'update_cliente',
        'encabezados': {
            "nombre":'NOMBRE',
            "primer_apellido":"PRIMER APELLIDO",
            "segundo_apellido":"SEGUNDO APELLIDO", 
            "cvetipopersona":"TIPO",
            "correo":"CORREO",
            },
    }
    return HttpResponse(template.render(context, request))


def add_cliente(request):
    form = PersonaPrincipalForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(lista_servicio)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo cliente", "form": form, 'regresa':'clientes'}
    return HttpResponse(template.render(context, request))   

def update_cliente(request):
    form = PersonaPrincipalForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(lista_servicio)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo cliente", "form": form, 'regresa':'clientes'}
    return HttpResponse(template.render(context, request))   


def lista_tipo_cliente(request):
    eventos_list = TipoPersona.objects.all().order_by('clave').values()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': eventos_list,
        'titulo': "Tipo Cliente",
        'add':"add_tipo_cliente",
        'add_label':'Nuevo Tipo Cliente',
        'update':'update_tipo_cliente',        
        'detalle':'detalle_tipo_cliente',
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

def update_tipo_cliente(request, id_actividad):
    actividad = get_object_or_404(TipoClienteForm, pk=id_actividad)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=actividad)
        if form.is_valid():
            form.save()
            return redirect(lista_tipo_cliente)
    else:
        form = EventoForm(instance=actividad)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': actividad, 'titulo': "Actualiza Tipo Cliente", "form": form, 'regresa':'lista_tipo_cliente'}
    return HttpResponse(template.render(context, request))

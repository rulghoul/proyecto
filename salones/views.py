from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from salones.models import TipoActividad, TipoEvento, TipoServicio
from .forms import ActividadForm, EventoForm, ServicioForm

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
    actividad_list = TipoActividad.objects.all()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': actividad_list,
        'titulo': "Actividades",
        'add':"add_actividad",
        'add_label':'Nueva actividad',
        'update':'update_actividad',
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))

def lista_evento(request):
    eventos_list = TipoEvento.objects.all()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': eventos_list,
        'titulo': "Eventos",
        'add':"add_evento",
        'add_label':'Nuevo Evento',
        'update':'update_evento',
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))


def lista_servicio(request):
    servicio_list = TipoServicio.objects.all()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': servicio_list,
        'titulo': "Servicios",
        'add':"add_servicio",
        'add_label':'Nuevo Servicio',
        'update':'update_servicio',
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


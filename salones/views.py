from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from salones.models import TipoActividad, TipoEvento, TipoServicio
from .forms import ActividadForm, EventoForm, ServicioForm

class ActividadCreateView(CreateView):
    model = TipoActividad
    fields = ('cvetipoactividad', 'desctipoactividad')

class EventoCreateView(CreateView):
    model = TipoEvento
    fields = ('cvetipoevento', 'desctipoevento')

class ServicioCreateView(CreateView):
    model = TipoServicio
    fields = ('cvetiposervicio', 'descservicio')

def add_actividad(request):
    form = ActividadForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request,"salones/actividad_form.html",{'form':form})


def add_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request,"salones/evento_form.html",{'form':form})

def add_servicio(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request,"salones/servicio_form.html",{'form':form})    



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


def lista_evento(request):
    eventos_list = TipoEvento.objects.all()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'eventos_list': eventos_list,
        'titulo': "Eventos",
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))

def update_evento(request, id_evento):
    evento = get_object_or_404(TipoEvento, pk=id_evento)
    form = EventoForm(instance=evento)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': evento, 'titulo': "Evento", "form": form}
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
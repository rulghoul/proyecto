from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from salones.models import Salon, TipoSalon, Direccion, Servicio
from .forms import SalonForm

class SalonCreateView(CreateView):
    model = Salon
    fields = ('nombre', 'tipo', 'servicios', 'direccion', 'imagenes')

def add_salon(request):
    form = SalonForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request,"salones/salon_form2.html",{'form':form})

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SalonSerializer, DireccionSerializer, TipoSalonSerializer, ServicioSerializer


class TipoSalonViewSet(viewsets.ModelViewSet):
    queryset = TipoSalon.objects.all()
    serializer_class = TipoSalonSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [permissions.IsAuthenticated]

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
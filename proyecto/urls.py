from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView
from salones.views import (
    user_login,           
    home_view,
    lista_actividad, add_actividad, update_actividad, ActividadViewSet,
    lista_evento, add_evento, update_evento, EventoViewSet,
    lista_servicio, add_servicio,  update_servicio, ServicioViewSet,
    eventos, add_evento_completo, update_evento_completo,
    lista_tipo_persona, add_tipo_cliente, update_tipo_cliente,
    personas, add_cliente, update_cliente,
)

from django.contrib.auth import views as auth_views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'actividades', ActividadViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'servicios', ServicioViewSet)

path_tipo_actividades = [
    path('lista_actividad', lista_actividad, name='lista_actividad'),
    path('add_actividad/', add_actividad, name='add_salon'),
    path('actividad/<int:id_actividad>/', update_actividad, name='update_actividad')
]

path_tipo_eventos = [
    path('lista_evento', lista_evento.as_view(), name='lista_evento'),
    path('add_evento/', add_evento, name='add_evento'),
    path('evento/<int:pk>/', update_evento.as_view(), name='update_evento'),
]

path_tipo_servicios = [
    path('lista_servicio', lista_servicio, name='lista_servicio'),
    path('add_servicio/', add_servicio, name='add_servicio'),
    path('servicio/<int:id_servicio>/', update_servicio, name='update_servicio')  
]

path_tipo_personas = [
    path('lista_tipo_cliente', lista_tipo_persona.as_view(), name='lista_tipo_cliente'),
    path('add_tipo_cliente', add_tipo_cliente, name='add_tipo_cliente'),
    path('update_tipo_cliente/<int:id_tipo_persona>/', update_tipo_cliente, name='update_tipo_cliente')
]

path_personas = [
    path('clientes', personas.as_view(), name='clientes'),
    path('add_cliente', add_cliente, name='add_cliente'),
    path('update_cliente/<int:id_persona>/', update_cliente, name='update_cliente')
]

path_eventos = [
    path('eventos', eventos.as_view(), name='eventos'),
    path('add_evento_completo', add_evento_completo, name='add_evento_completo'),
    path('update_evento_completo/<int:id_evento>/', update_evento_completo, name='update_evento_completo')
]

urlpatterns = [

    path('', home_view, name='home'),    
    path('login/', user_login, name='user_login'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), 
    #Empieza la parte Rest
    path('json/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #termina la parte rest

] + path_tipo_actividades  \
+ path_tipo_eventos \
+ path_tipo_servicios \
+ path_tipo_personas \
+ path_personas \
+ path_eventos #\

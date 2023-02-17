from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView
from salones.views.catalogos01 import (
    user_login,           
    home_view,
    lista_actividad, add_actividad, update_actividad, detalle_actividad , borra_actividad, ActividadViewSet,
    lista_evento, add_evento, update_evento, detalle_evento,borra_tipo_evento, EventoViewSet,
    lista_servicio, add_servicio, update_servicio, detalle_servicio, borra_servicio,ServicioViewSet,
    eventos, add_evento_completo, update_evento_completo, borra_evento_completo, detail_evento_completo,
    add_evento_detalle, update_evento_detalle, borra_evento_detalle, detail_evento_detalle,
    lista_tipo_persona, add_tipo_cliente, update_tipo_cliente, borra_tipo_persona, detalle_tipo_persona,
    personas, add_cliente, detalle_persona, borra_persona, update_cliente,
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
    path('detalle_actividad/<int:pk>', detalle_actividad.as_view(), name='detalle_actividad'),
    path('actividad/<int:id_actividad>/', update_actividad, name='update_actividad'),
    path('borra_actividad/<int:pk>/', borra_actividad.as_view(), name='borra_actividad'),
]

path_tipo_eventos = [
    path('lista_evento', lista_evento.as_view(), name='lista_evento'),
    path('add_evento/', add_evento, name='add_evento'),
    path('detalle_evento/<int:pk>', detalle_evento.as_view(), name='detalle_evento'),
    path('evento/<int:pk>/', update_evento.as_view(), name='update_evento'),
    path('borra_tipo_evento/<int:pk>/', borra_tipo_evento.as_view(), name='borra_evento'),
]

path_tipo_servicios = [
    path('lista_servicio', lista_servicio, name='lista_servicio'),
    path('add_servicio/', add_servicio, name='add_servicio'),
    path('detalle_servicio/<int:pk>', detalle_servicio.as_view(), name='detalle_servicio'),
    path('servicio/<int:id_servicio>/', update_servicio, name='update_servicio'),
    path('borra_servicio/<int:pk>/', borra_servicio.as_view(), name='borra_servivio'),
]

path_tipo_personas = [
    path('lista_tipo_cliente', lista_tipo_persona.as_view(), name='lista_tipo_cliente'),
    path('add_tipo_cliente', add_tipo_cliente, name='add_tipo_cliente'),
    path('detalle_tipo_persona/<int:pk>', detalle_tipo_persona.as_view(), name='detalle_tipo_persona'),
    path('update_tipo_cliente/<int:id_tipo_persona>/', update_tipo_cliente, name='update_tipo_cliente'),
    path('borra_tipo_persona/<int:pk>/', borra_tipo_persona.as_view(), name='borra_tipo_persona'),
]

path_personas = [
    path('clientes', personas.as_view(), name='clientes'),
    path('add_cliente', add_cliente, name='add_cliente'),
    path('update_cliente/<int:id_persona>/', update_cliente, name='update_cliente'),
    path('borra_cliente/<int:pk>/', borra_persona.as_view(), name='borra_cliente'),
    path('detalle_cliente/<int:pk>/', detalle_persona.as_view(), name='detalle_cliente'),
]

path_eventos = [
    path('eventos', eventos.as_view(), name='eventos'),
    path('add_evento_completo', add_evento_completo.as_view(), name='add_evento_completo'),
    path('update_evento_completo/<int:pk>/', update_evento_completo.as_view(), name='update_evento_completo'),
    path('borra_evento_completo/<int:pk>/', borra_evento_completo.as_view(), name='borra_evento_completo'),
    path('detail_evento_completo/<int:pk>/', detail_evento_completo.as_view(), name='detail_evento_completo'),
]

path_evento_detalle = [
    path('add_evento_detalle/<int:pk>', add_evento_detalle.as_view(), name='add_evento_detalle'),
    path('update_evento_detalle/<int:pk>/', update_evento_detalle.as_view(), name='update_evento_detalle'),
    path('borra_evento_detalle/<int:pk>/', borra_evento_detalle.as_view(), name='borra_evento_detalle'),
    path('detail_evento_detalle/<int:pk>/', detail_evento_detalle.as_view(), name='detail_evento_detalle'),

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
+ path_eventos \
+ path_evento_detalle #\

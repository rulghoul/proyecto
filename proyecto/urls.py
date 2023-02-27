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
    load_clases_servicio, load_desglose_servicio,
)

from django.contrib.auth import views as auth_views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'actividades', ActividadViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'servicios', ServicioViewSet)

inicio = ''

path_tipo_actividades = [
    path(f'{inicio}muestra/lista_actividad', lista_actividad, name='lista_actividad'),
    path(f'{inicio}add_actividad/', add_actividad, name='add_salon'),
    path(f'{inicio}detalle_actividad/<int:pk>', detalle_actividad.as_view(), name='detalle_actividad'),
    path(f'{inicio}actividad/<int:id_actividad>/', update_actividad, name='update_actividad'),
    path(f'{inicio}borra_actividad/<int:pk>/', borra_actividad.as_view(), name='borra_actividad'),
]

path_tipo_eventos = [
    path(f'{inicio}lista_evento', lista_evento.as_view(), name='lista_evento'),
    path(f'{inicio}add_evento/', add_evento, name='add_evento'),
    path(f'{inicio}detalle_evento/<int:pk>', detalle_evento.as_view(), name='detalle_evento'),
    path(f'{inicio}evento/<int:pk>/', update_evento.as_view(), name='update_evento'),
    path(f'{inicio}borra_tipo_evento/<int:pk>/', borra_tipo_evento.as_view(), name='borra_evento'),
]

path_tipo_servicios = [
    path(f'{inicio}lista_servicio', lista_servicio, name='lista_servicio'),
    path(f'{inicio}add_servicio/', add_servicio, name='add_servicio'),
    path(f'{inicio}detalle_servicio/<int:pk>', detalle_servicio.as_view(), name='detalle_servicio'),
    path(f'{inicio}servicio/<int:id_servicio>/', update_servicio, name='update_servicio'),
    path(f'{inicio}borra_servicio/<int:pk>/', borra_servicio.as_view(), name='borra_servivio'),
]

path_tipo_personas = [
    path(f'{inicio}lista_tipo_cliente', lista_tipo_persona.as_view(), name='lista_tipo_cliente'),
    path(f'{inicio}add_tipo_cliente', add_tipo_cliente, name='add_tipo_cliente'),
    path(f'{inicio}detalle_tipo_persona/<int:pk>', detalle_tipo_persona.as_view(), name='detalle_tipo_persona'),
    path(f'{inicio}update_tipo_cliente/<int:id_tipo_persona>/', update_tipo_cliente, name='update_tipo_cliente'),
    path(f'{inicio}borra_tipo_persona/<int:pk>/', borra_tipo_persona.as_view(), name='borra_tipo_persona'),
]

path_personas = [
    path(f'{inicio}clientes', personas.as_view(), name='clientes'),
    path(f'{inicio}add_cliente', add_cliente, name='add_cliente'),
    path(f'{inicio}update_cliente/<int:id_persona>/', update_cliente, name='update_cliente'),
    path(f'{inicio}borra_cliente/<int:pk>/', borra_persona.as_view(), name='borra_cliente'),
    path(f'{inicio}detalle_cliente/<int:pk>/', detalle_persona.as_view(), name='detalle_cliente'),
]

path_eventos = [
    path(f'{inicio}eventos', eventos.as_view(), name='eventos'),
    path(f'{inicio}add_evento_completo', add_evento_completo.as_view(), name='add_evento_completo'),
    path(f'{inicio}update_evento_completo/<int:pk>/', update_evento_completo.as_view(), name='update_evento_completo'),
    path(f'{inicio}borra_evento_completo/<int:pk>/', borra_evento_completo.as_view(), name='borra_evento_completo'),
    path(f'{inicio}detail_evento_completo/<int:pk>/', detail_evento_completo.as_view(), name='detail_evento_completo'),
]

path_evento_detalle = [
    path(f'{inicio}add_evento_detalle/<int:pk>', add_evento_detalle.as_view(), name='add_evento_detalle'),
    path(f'{inicio}update_evento_detalle/<int:pk>/', update_evento_detalle.as_view(), name='update_evento_detalle'),
    path(f'{inicio}borra_evento_detalle/<int:pk>/', borra_evento_detalle.as_view(), name='borra_evento_detalle'),
    path(f'{inicio}detail_evento_detalle/<int:pk>/', detail_evento_detalle.as_view(), name='detail_evento_detalle'),
]

path_dropdown = [
    path('ajax/load_clases_servicio/', load_clases_servicio, name='ajax_load_clases_servicio'), 
    path('ajax/load_desglose_servicio/', load_desglose_servicio, name='ajax_load_desglose_servicio'), 
]

urlpatterns = [

    path(f'{inicio}', home_view, name='home'),    
    path(f'{inicio}login/', user_login, name='user_login'),
    path(f'{inicio}change-password/', auth_views.PasswordChangeView.as_view()),
    path(f'{inicio}admin/', admin.site.urls),
    path(f'{inicio}accounts/', include("django.contrib.auth.urls")), 
    #Empieza la parte Rest
    path(f'{inicio}json/', include(router.urls)),
    path(f'{inicio}api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #termina la parte rest

] + path_tipo_actividades  \
+ path_tipo_eventos \
+ path_tipo_servicios \
+ path_tipo_personas \
+ path_personas \
+ path_eventos \
+ path_evento_detalle \
+ path_dropdown #\

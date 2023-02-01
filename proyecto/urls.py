from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView
from salones.views import (
    user_login, 
    add_actividad, ActividadViewSet, add_evento, EventoViewSet, 
    add_servicio, ServicioViewSet, 
    lista_evento, 
    update_evento, 
    lista_actividad, 
    update_actividad, 
    lista_servicio, 
    update_servicio, 
    home_view, 
    detalle_actividad, 
    detalle_evento, 
    detalle_servicio,
    EventoCreateView,
    ActividadCreateView,
    ServicioCreateView,
    eventos,
    add_evento_completo,
    update_evento_completo,
    personas,
    add_cliente,
    update_cliente,
    lista_tipo_cliente,
    lista_tipo_persona,
    add_tipo_cliente,
    update_tipo_cliente,
    )
from django.contrib.auth import views as auth_views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'actividades', ActividadViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'servicios', ServicioViewSet)

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), 
    #Empieza la parte Rest
    path('json/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #termina la parte rest
    path('', home_view, name='home'), 
    #path('add_salon/', add_salon, name='add_salon'),
    path('add_actividad/', add_actividad, name='add_salon'),
    path('add_evento/', add_evento, name='add_evento'),
    path('add_servicio/', add_servicio, name='add_servicio'),
    path('lista_actividad', lista_actividad, name='lista_actividad'),
    path('lista_evento', lista_evento.as_view(), name='lista_evento'),
    path('lista_servicio', lista_servicio, name='lista_servicio'),
    path('actividad/<int:id_actividad>/', update_actividad, name='update_actividad'),
    path('evento/<int:id_evento>/', update_evento, name='update_evento'),
    path('servicio/<int:id_servicio>/', update_servicio, name='update_servicio'),    
    path('actividad_detalle/<int:id_actividad>/', detalle_actividad, name='detalle_actividad'),
    path('evento_detalle/<int:id_evento>/', detalle_evento, name='detalle_evento'),
    path('servicio_detalle/<int:id_servicio>/', detalle_servicio, name='detalle_servicio'),
    path('add_accion_modal/', ActividadCreateView.as_view(), name='add_accion_modal'),
    path('add_evento_modal/', EventoCreateView.as_view(), name='add_evento_modal'),
    path('add_evento_modal/', ServicioCreateView.as_view(), name='add_servicio_modal'),
    path('eventos', eventos.as_view(), name='eventos'),
    path('add_evento_completo', add_evento_completo, name='add_evento_completo'),
    path('update_evento_completo/<int:id_evento>/', update_evento_completo, name='update_evento_completo'),
    path('clientes', personas.as_view(), name='clientes'),
    path('add_cliente', add_cliente, name='add_cliente'),
    path('update_cliente/<int:id_persona>/', update_cliente, name='update_cliente'),
    path('lista_tipo_cliente', lista_tipo_persona.as_view(), name='lista_tipo_cliente'),
    path('add_tipo_cliente', add_tipo_cliente, name='add_tipo_cliente'),
    path('update_tipo_cliente/<int:id_tipo_persona>/', update_tipo_cliente, name='update_tipo_cliente'),
]

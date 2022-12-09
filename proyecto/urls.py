from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView
from salones.views import user_login, add_actividad, ActividadViewSet, add_evento, EventoViewSet, add_servicio, ServicioViewSet, lista_evento, update_evento, lista_actividad, update_actividad, lista_servicio, update_servicio, home_view
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
    path('lista_evento', lista_evento, name='lista_evento'),
    path('lista_servicio', lista_servicio, name='lista_servicio'),
    path('actividad/<int:id_actividad>/', update_actividad, name='update_actividad'),
    path('evento/<int:id_evento>/', update_evento, name='update_evento'),
    path('servicio/<int:id_servicio>/', update_servicio, name='update_servicio'),
]

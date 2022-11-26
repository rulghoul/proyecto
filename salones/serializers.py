from .models import Salon, Direccion, Servicio, TipoSalon, Imagen
from rest_framework import serializers


class SalonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salon
        fields = ['nombre', 'direccion', 'tipo', 'servicios', 'imagenes']


class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'colonia', 'municipio', 'codigo_postal']

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion']


class TipoSalonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoSalon
        fields = ['nombre', 'descripcion']
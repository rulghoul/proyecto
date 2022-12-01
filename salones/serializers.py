from .models import TipoActividad, TipoEvento, TipoServicio
from rest_framework import serializers


class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoActividad
        fields = ['cvetipoactividad', 'desctipoactividad']


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoEvento
        fields = ['cvetipoevento', 'desctipoevento']

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoServicio
        fields = ['cvetiposervicio', 'descservicio']


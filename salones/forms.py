from django import forms
from salones.models import TipoActividad, TipoEvento, TipoServicio

class ActividadForm(forms.ModelForm):
    class Meta:
        model = TipoActividad
        fields = ('cvetipoactividad', 'desctipoactividad', 'bandactivo')

class EventoForm(forms.ModelForm):
    class Meta:
        model = TipoEvento
        #fields = ('cvetipoevento', 'desctipoevento', 'bandactivo')
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = TipoServicio
        fields = ('cvetiposervicio', 'descservicio', 'bandactivo')

#from django.forms import inlineformset_factory
#SalonFormSet = inlineformset_factory(Salon, Direccion, fields=('nombre', 'tipo', 'servicios',))
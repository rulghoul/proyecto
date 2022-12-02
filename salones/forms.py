from django import forms
from salones.models import TipoActividad, TipoEvento, TipoServicio

class ActividadForm(forms.ModelForm):
    class Meta:
        model = TipoActividad
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = TipoEvento
        #fields = ('cvetipoevento', 'desctipoevento', 'bandactivo')
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = TipoServicio
        fields = '__all__'

#from django.forms import inlineformset_factory
#SalonFormSet = inlineformset_factory(Salon, Direccion, fields=('nombre', 'tipo', 'servicios',))
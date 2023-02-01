from django import forms
from salones.models import (
    TipoActividad, 
    TipoEvento, 
    TipoServicio,
    TipoPersona, 
    EncEvento,
    PersonaPrincipal)

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


class EventoCompletoForm(forms.ModelForm):
    class Meta:
        model = EncEvento
        fields = ['cvetipoevento', 'cvepersona', 'nombre', 'banaprovada']


class TipoClienteForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = '__all__'


class PersonaPrincipalForm(forms.ModelForm):
    class Meta:
        model = PersonaPrincipal
        fields = '__all__'


#from django.forms import inlineformset_factory
#SalonFormSet = inlineformset_factory(Salon, Direccion, fields=('nombre', 'tipo', 'servicios',))

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class EventoFormModal(BSModalModelForm):
    class Meta:
        model = EncEvento
        fields = '__all__'
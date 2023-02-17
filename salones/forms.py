from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select, CheckboxInput
from salones.models import (
    TipoActividad, 
    TipoEvento, 
    TipoServicio,
    TipoPersona, 
    EncEvento,
    PersonaPrincipal)

class ActividadForm(ModelForm):
    class Meta:
        model = TipoActividad
        fields = '__all__'

class EventoForm(ModelForm):
    class Meta:
        model = TipoEvento
        #fields = ('cvetipoevento', 'desctipoevento', 'bandactivo')
        fields = '__all__'

class ServicioForm(ModelForm):
    class Meta:
        model = TipoServicio
        fields = '__all__'


class EventoCompletoForm(ModelForm):
    class Meta:
        model = EncEvento
        fields = ['cvetipoevento', 'cvepersona', 'nombre', 
                  'numeropersonas', 'opcion', 'banaprovada',  
                  ]
        widgets = {
            'cvetipoevento': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 3rem;',
                }),
            'cvepersona': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 3rem;',
                }),
            'nombre': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 3rem;',
                'placeholder': 'nombre'
                }),
            'numeropersonas': NumberInput(attrs={
                'class': "form-control disable", 
                'style': 'max-width: 300px; border-radius: 3rem;',
                'placeholder': 'numero de personas'
                }),
            'opcion': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 50px; border-radius: 3rem;',
                }),
            'banaprovada': CheckboxInput(attrs={
                'class': "form-control",
                }),

        }


class TipoClienteForm(ModelForm):
    class Meta:
        model = TipoPersona
        fields = '__all__'


class PersonaPrincipalForm(ModelForm):
    class Meta:
        model = PersonaPrincipal
        fields = '__all__'


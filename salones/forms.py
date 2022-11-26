from django import forms
from salones.models import Salon, Direccion

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('nombre', 'tipo', 'servicios',  'imagenes')

#from django.forms import inlineformset_factory
#SalonFormSet = inlineformset_factory(Salon, Direccion, fields=('nombre', 'tipo', 'servicios',))
#from typing import Any, Dict
from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','descripcion','precio','fecha_registro','estatus']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')             #Deben empatar con los atributos en mi modelo
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fecha_registro = cleaned_data.get('fecha_registro')
        estatus = cleaned_data.get('estatus')

        if not nombre or not descripcion or not precio or not fecha_registro or not estatus:
            raise forms.ValidationError("Todos Los Campos Deben Ser Completados")
        return cleaned_data
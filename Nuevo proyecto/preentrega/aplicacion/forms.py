from django import forms 

class EquipoForm(forms.Form):
    nombre = forms.CharField (max_length=60, required=True) 
    
class GoleadorForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    apellido = forms.CharField(max_length=60, required=True)
    
    
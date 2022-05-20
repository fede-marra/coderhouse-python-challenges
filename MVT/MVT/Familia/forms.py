from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=30)
    apellido = forms.CharField(label="Apellido",max_length=30)
    nacimiento = forms.DateField(label="Nacimiento")
    documento = forms.IntegerField(label="Documento")
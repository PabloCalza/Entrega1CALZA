from django import forms

class MedicosForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    matricula=forms.IntegerField()
    email=forms.EmailField()

class EnfermerasForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    matricula=forms.IntegerField()
    email=forms.EmailField()

class PacientesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    email=forms.EmailField()
from django import forms
from appcore.models import Pelicula,Serie,Genero

class peliform(forms.ModelForm):
    class Meta:
        model=Pelicula
        fields=["tipo","nombre","duracion","genero","calificacion"]

class serieform(forms.ModelForm):
    class Meta:
        model=Serie
        fields=["tipo","nombre","duracion","genero","calificacion"]

class generoform(forms.ModelForm):
    class Meta:
        model=Genero
        fields=["genero"]

class buscarform(forms.Form):
    nombre=forms.IntegerField(label='nombre')
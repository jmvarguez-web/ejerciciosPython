from django import forms
from director_cine.models import Director, Pelicula


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'



class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
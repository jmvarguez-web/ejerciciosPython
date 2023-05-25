from django.shortcuts import render
from django.http import HttpResponse
from .models import Director, Genero ,Pelicula
def index(request):
    num_directores = Director.objects.all().count()
    num_genero = Genero.objects.all().count()
    num_pelicula=Pelicula.objects.all().count()

    return render(
        request,'pages/index.html',
        context={
            'num_directores':num_directores,
            'num_genero':num_genero,
            'num_pelicula': num_pelicula,
        }
    )

# Create your views here.

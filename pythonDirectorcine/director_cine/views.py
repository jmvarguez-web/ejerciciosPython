from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import DirectorForm
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
def listar_directores(request):
    directores = Director.objects.all()
    return render(
        request, 'pages/listar_directores.html',
        context={
            'directores': directores,
            'pagina': 'directores',
            'titulo': 'Listar Directores',
        }
    )

def editar_director(request, id):
    director = get_object_or_404(Director, pk=id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DirectorForm(request.POST, instance=director)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('directores')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'editar-director.html', {'form': form, 'pagina': 'directores', 'titulo': 'Editar Director', 'modo': 'editar'})

def eliminar_director(request, id):
    director = get_object_or_404(Director, pk=id)
    if director:
        director.delete()
        #url = reverse('listar_directores')
        return redirect('index')
def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(
        request, 'pages/listar_peliculas.html',
        context={
            'peliculas': peliculas,
            'pagina': 'directores',
            'titulo': 'Listar Peliculas',
        }
    )

def listar_generos(request):
    generos = Genero.objects.all()
    return render(
        request, 'pages/listar_generos.html',
        context={
            'generos': generos,
            'pagina': 'generos',
            'titulo': 'Listar Generos',
        }
    )
# Create your views here.

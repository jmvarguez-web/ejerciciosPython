from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
        path('', views.index, name='index'),
        path('listar_directores/', views.listar_directores, name='Lista directores'),
        path('listar_peliculas/', views.listar_peliculas, name='Lista directores'),
        path('listar_generos/', views.listar_generos, name='Lista directores'),
        path('eliminar-director/<int:id>',
             views.eliminar_director, name='eliminar-director'),
]

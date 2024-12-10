from django.shortcuts import render,redirect
from .models import Pelicula,Serie,Genero
from .forms import peliform,serieform,generoform, buscarform
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request,"appcore/inicio.html")

#pelis

def pelis(request):
    lista_pelis=Pelicula.objects.all()
    contexto={"lista_pelis":lista_pelis}
    return render(request, "appcore/pelis.html",contexto)

def creapeli(request):
    if request.method=='POST':
        form=peliform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pelis')
    else:
        form=peliform()
        contexto={'form':form}
    return render(request,"appcore/creapeli.html",contexto)


#series

def series(request):
    lista_series=Serie.objects.all()
    contexto={"lista_series":lista_series}
    return render(request,"appcore/series.html",contexto)

def creaserie(request):
    if request.method=='POST':
        form=serieform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('series')
    else:
        form=serieform()
        contexto={'form':form}
    return render(request,"appcore/creaserie.html",contexto)

#generos

def generos(request):
    lista_genero=Genero.objects.all()
    contexto={'lista_genero':lista_genero}
    return render(request,"appcore/generos.html",contexto)

def creagenero(request):
    if request.method=='POST':
        form=generoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generos')
    else:
        form=generoform()
        contexto={'form':form}
    return render(request,"appcore/creagenero.html",contexto)

def buscarpeli(request):
    if request.method=='GET':
        form=buscarform(request.GET)
        if form.is_valid():
            nombre= form.cleaned_data['nombre']
            resultados=Pelicula.objects.filter(nombre=nombre)
        return render(request,"appcore/buscarpeli.html",{'resultados':resultados,'form':form})
    
    else:
        form=buscarform()
        return render(request,"appcore/buscarpeli.html",{'form':form})

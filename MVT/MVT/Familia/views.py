from django.http import HttpResponseBadRequest, HttpResponseRedirect
from Familia.models import familiares
from django.shortcuts import render
from Familia.forms import PersonaForm
from django.contrib import messages



def Mostrar(request):
    flia = familiares.objects.all
    diccionario = {"personas":flia}
    return render(request,"mostrar.html",diccionario)

def Agregar(request):

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data['apellido']
            nacimiento = form.cleaned_data['nacimiento']
            documento = form.cleaned_data['documento']
            familiares.objects.create(nombre=nombre, apellido=apellido,nacimiento=nacimiento,documento=documento)
            messages.success(request, 'El familiar fue agregado correctamente')
        return HttpResponseRedirect("/Familia/")

    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    return render(request,'agregar.html',{'form':form})

def Borrar(request, identificador):

    if request.method == "GET":
        persona = familiares.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
            messages.success(request, 'El item fue eliminado correctamente')
        return HttpResponseRedirect("/Familia/")
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo request")


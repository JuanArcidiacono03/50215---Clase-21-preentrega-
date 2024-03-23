from django.shortcuts import render, redirect 
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")
    

def equipos(request):
    contexto = {'equipo': Equipo.objects.all().order_by("id")} 
    return render(request, "aplicacion/equipos.html",contexto )

def posiciones(request):
    contexto = {'posicion': Posicion.objects.all()}
    return render(request, "aplicacion/posiciones.html",contexto)  

def goleadores(request):
    contexto = {'goleador': Goleador.objects.all()}
    return render(request, "aplicacion/goleadores.html", contexto)

#________________________________________ Adicionales
def acerca(request):
    return render(request, "aplicacion/acerca.html") 



#________________Forms
#________________Equipos

def equipoCreate(request):
    if request.method == "POST":
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            equipo_nombre = miForm.cleaned_data.get("nombre")
            equipo = Equipo(nombre=equipo_nombre)
            equipo.save()
            return redirect(reverse_lazy('equipos'))


    else: 
          miForm = EquipoForm() 
    return render(request, "aplicacion/equipoForm.html", {"form": miForm})

def equipoUpdate(request , id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    if request.method == "POST":
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            equipo.nombre = miForm.cleaned_data.get("nombre")
            equipo.save()
            return redirect(reverse_lazy('equipos'))

    else: 
          miForm = EquipoForm(initial={'nombre':equipo.nombre}) 
    return render(request, "aplicacion/equipoForm.html", {"form": miForm})

def equipoDelete(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    equipo.delete()
    return redirect(reverse_lazy('equipos'))

#__________________________Create/Update Goleador

def goleadorCreate(request):
    if request.method == "POST":
        miForm = GoleadorForm(request.POST)
        if miForm.is_valid():
            goleador_nombre = miForm.cleaned_data.get("nombre")
            goleador = Goleador(nombre=goleador_nombre)
                                
            goleador.save()
           
            return redirect(reverse_lazy('goleadores'))

    else: 
          miForm = GoleadorForm() 
    return render(request, "aplicacion/goleadorForm.html", {"form": miForm})


def goleadorUpdate(request, id_goleador):
    goleador = Goleador.objects.get(id=id_goleador)
    if request.method == "POST":
        miForm = GoleadorForm(request.POST)
        if miForm.is_valid():
            goleador.nombre = miForm.cleaned_data.get("nombre") 
            goleador.apellido = miForm.cleaned_data.get("apellido")  
            goleador.save()
            return redirect(reverse_lazy('goleadores'))


    else: 
          miForm = EquipoForm(initial={'nombre': goleador.nombre ,'apellido': goleador.apellido,}) 
    return render(request, "aplicacion/goleadorForm.html", {"form": miForm})


def goleadorDelete(request, id_goleador):
    goleador = Goleador.objects.get(id=id_goleador)
    goleador.delete()
    return redirect(reverse_lazy('goleadores'))




#_____________________________Busqueda

def buscarEquipos(request):
    return render(request, "aplicacion/buscar.html")

def encontrarEquipos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Equipo.objects.filter(nombre__icontains=patron)
        contexto = {"equipos": equipos}
        return render(request, "aplicacion/equipos.html", contexto)


#_____________________________Posiciones
 
class PosicionList(ListView):
    model = Posicion
    
class PosicionCreate(CreateView):
    model = Posicion
    fields = ["nombre"]
    success_url = reverse_lazy("posiciones")
      
class PosicionUpdate(UpdateView):
    model = Posicion
    fields = ["nombre"]
    success_url = reverse_lazy("posiciones")
    
class PosicionDelete(DeleteView):
    model = Posicion
    success_url = reverse_lazy("posiciones")
    
    

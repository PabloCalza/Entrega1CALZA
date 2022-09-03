from django.shortcuts import render
from django.http import HttpResponse
from AppCalza.forms import MedicosForm, EnfermerasForm, PacientesForm
from AppCalza.models import Medicos, Enfermeras, Pacientes

def inicio(request):
    return render (request, "AppCalza/inicio.html")
def medicos(request):
    return render (request, "AppCalza/medicos.html")
def enfermeras(request):
    return render (request, "AppCalza/enfermeras.html")
def pacientes (request):
    return render (request, "AppCalza/pacientes.html")

def medicos(request):
    if request.method=="POST":
        form=MedicosForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            matricula=informacion["matricula"]
            email=informacion["email"]
            medico=Medicos(nombre=nombre, apellido=apellido, matricula=matricula, email=email)
            medico.save()
            return render (request, "AppCalza/inicio.html")
            
            
    else:
        formulario=MedicosForm()
    return render (request, "AppCalza/medicos.html", {"formulario":formulario})

def enfermeras(request):
    if request.method=="POST":
        form=EnfermerasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            matricula=info["matricula"]
            email=info["email"]
            enfermera=Enfermeras(nombre=nombre, apellido=apellido, matricula=matricula, email=email)
            enfermera.save()
            return render (request, "AppCalza/inicio.html")
            
            
    else:
        formulario=EnfermerasForm()
    return render (request, "AppCalza/enfermeras.html", {"formulario":formulario})

def pacientes(request):
    if request.method=="POST":
        form=PacientesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            edad=info["edad"]
            email=info["email"]
            paciente=Pacientes(nombre=nombre, apellido=apellido, edad=edad, email=email)
            paciente.save()
            return render (request, "AppCalza/inicio.html")
            
            
    else:
        formulario=PacientesForm()
    return render (request, "AppCalza/pacientes.html", {"formulario":formulario})



def busquedaMatricula(request):
    return render (request, "AppCalza/busquedaMatricula.html")

def buscar(request):
    if request.GET["matricula"]:
        matricula=request.GET["matricula"]
        medicos=Medicos.objects.filter(matricula=matricula)
        return render (request, "AppCalza/resultadosBusqueda.html", {"medicos":medicos})
    else:
        return render (request, "AppCalza/busquedaMatricula.html", {"mensaje":"ingrese matricula"})


    return HttpResponse (respuesta)
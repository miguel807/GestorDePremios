from warnings import catch_warnings

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from AppLoginPremios.form import authenticationForm,userCreationForm
from AppLoginPremios.models import Premios,Obrass,Cronograma,Jurado


#username =Miguel
#password =migue@123

def Login(request):


    # retornar el formulario de autenticacion
    return render(request,"Login.html",{"form":authenticationForm})

@login_required()
def Home(request):

    #Eliminar registro
    if request.method == 'GET':
        nombreUserEliminar = request.GET.get("nombreUserInput","")
        obraIdEliminar = request.GET.get("obraId")
        nombreObra = request.GET.get("nombreObra","")
        nombrePremio = request.GET.get("nombrePremio","")
        idJurado  = request.GET.get("juradoID","")
        idCronograma = request.GET.get("cronogramaID","")
        if idJurado != "":
            id = int(idJurado)
            datoEliminar = Jurado.objects.get(id=id)
            datoEliminar.delete()

        if idCronograma != "":
            id = int(idCronograma)
            datoEliminar = Cronograma.objects.get(id=id)
            datoEliminar.delete()
        if obraIdEliminar != -1 and nombreUserEliminar != "" and nombreObra != "" and nombrePremio != "":

           datoEliminar = User.objects.get(username=nombreUserEliminar)
           datoObra = datoEliminar.premios.filter(id=obraIdEliminar)
           copiaDatoObra = datoObra
           datoObra.delete()

        # datos para eliminar obra

        if obraIdEliminar != -1 and nombreUserEliminar != "" and nombreObra != "" and nombrePremio == "":
           datoEliminar = User.objects.get(username=nombreUserEliminar)
           datoObra = datoEliminar.obrass.filter(id=obraIdEliminar)
           copiaDatoObra = datoObra
           datoObra.delete()


    if request.method=='POST':
        newUser = request.POST.get("newPremioArtista","")
        newObra = request.POST.get("newPremioNombreObra", "")
        newPremio = request.POST.get("newPremio", "")
        newFacultad =  request.POST.get("newPremioFacultad", "")
        newManifestacion = request.POST.get("newPremioManifestacion", "")
        newNombreJ = request.POST.get("newNombreJurado", "")
        newOcupacionJ = request.POST.get("newOcupacion", "")
        newManifestacionJ = request.POST.get("newmanifestacion", "")
        newFechaC = request.POST.get("newNombreFecha","")
        newHoraC = request.POST.get("newHora","")
        newFacultadC = request.POST.get("newFacultadC","")
        newLugarC = request.POST.get("newLugarC","")


        if newUser != "" and newObra != "" and newFacultad != "" and newPremio !="" and newManifestacion != "":

            user = User.objects.get(username=newUser)
            nuevoPremio  = Premios(user=user,nombreObra=newObra,facultad=newFacultad,premio=newPremio,manifestacion=newManifestacion,existe=True)
            nuevoPremio.save()

        #guardando obra
        if newUser != "" and newObra != "" and newFacultad != "" and newPremio == "" and newManifestacion != "":
            user = User.objects.get(username=newUser)
            nuevaObra = Obrass(user=user, nombreObra=newObra, facultad=newFacultad,manifestacion=newManifestacion, existe=True)
            nuevaObra.save()
        #guardar Jurado
        if newNombreJ != "" and newOcupacionJ != "" and newManifestacionJ != "":
            newJurado = Jurado(nombreJurado=newNombreJ, ocupacion=newOcupacionJ,
                               manifestacionArtistica=newManifestacionJ)
            newJurado.save()

        #guardar Cronograma

        if newFechaC !="" and newHoraC != "" and newFacultadC!="" and newLugarC!="":
            newCronograma = Cronograma(fecha = newFechaC,hora = newHoraC,facultad = newFacultadC,lugar = newLugarC)
            newCronograma.save()

    return render(request,'Home.html')

@login_required()
def register(request):

    if request.method == 'POST':
        formCreateUser = userCreationForm(data=request.POST)
        if formCreateUser.is_valid():
            formCreateUser.save()
            return redirect("Home")

    return render(request,"register.html",{"formR":userCreationForm})

@login_required()
def Premioss(request,id):


    #Vista para el admin
    band=False
    user_id=""
    datos=""
    count = 0
    lista=[]
    copiaDatoObra=""
    refresh = False
    datos = User.objects.filter(premios__existe=True)
    Total = User.objects.filter(premios__existe=True).count()

    for user in datos:
        libros = user.premios.all()
        if band == False:
         for libro in libros:
            lista.append(libro)
            count=count+1
            if count==Total:
                band=True
                break

    #vista para el usuario normal
    # de todas maneras ver como se puede acceder a los datos del usuario mediante el auth
    userActual = User.objects.get(id=id)
    datosUserNormal = userActual.premios.all()
    cantidadNormal = userActual.premios.all().count()

 #Editando usuario
    if request.method == "POST":
        idObra = request.POST.get("obraId", "")

        usuario = User.objects.get(premios__id=idObra)
        datosEditar = usuario.premios.get(id=idObra)

        # nuevos datos
        nombreObraE = request.POST.get("nombreObraE", "")
        nombreFacultadE = request.POST.get("facultadE", "")
        nombrePremioE = request.POST.get("premioE", "")
        nombreManifestacionE = request.POST.get("manifestacionE", "")


        if nombreObraE != "" and nombreFacultadE != "" and nombrePremioE != "" and nombreManifestacionE != "":
            datosEditar.nombreObra = nombreObraE
            datosEditar.facultad = nombreFacultadE
            datosEditar.premio = nombrePremioE
            datosEditar.manifestacion = nombreManifestacionE
            datosEditar.save()


    return render(request,"Premios.html",{"datos":lista,"datosUserNormal":datosUserNormal,"cantidad":cantidadNormal,"datoObra":copiaDatoObra,"refresh":refresh})

@login_required()
def Obras(request,id):
    # Vista para el admin
    band = False
    user_id = ""
    datos = ""
    count = 0
    lista = []
    copiaDatoObra = ""

    datos = User.objects.filter(obrass__existe=True)
    Total = User.objects.filter(obrass__existe=True).count()

    for user in datos:
        libros = user.obrass.all()
        if band == False:
            for libro in libros:
                lista.append(libro)
                count = count + 1
                if count == Total:
                    band = True
                    break

    # vista para el usuario normal
    # de todas maneras ver como se puede acceder a los datos del usuario mediante el auth
    userActual = User.objects.get(id=id)
    datosUserNormal = userActual.obrass.all()
    cantidadNormal = userActual.obrass.all().count()

    # Editando usuario
    if request.method == "POST":
        idObra = request.POST.get("obraId", "")

        usuario = User.objects.get(obrass__id=idObra)
        datosEditar = usuario.obrass.get(id=idObra)

        # nuevos datos
        nombreObraE = request.POST.get("nombreObraE", "")
        nombreFacultadE = request.POST.get("facultadE", "")
        nombrePremioE = request.POST.get("premioE", "")
        nombreManifestacionE = request.POST.get("manifestacionE", "")

        if nombreObraE != "" and nombreFacultadE != "" and  nombreManifestacionE != "":
            datosEditar.nombreObra = nombreObraE
            datosEditar.facultad = nombreFacultadE
            datosEditar.manifestacion = nombreManifestacionE
            datosEditar.save()

    return render(request, "Obras.html", {"datos": lista, "datosUserNormal": datosUserNormal, "cantidad": cantidadNormal,"datoObra": copiaDatoObra})

@login_required()
def jurado(request):
    datos = Jurado.objects.all()

    return render(request,"Jurado.html",{"datos":datos})


def cronograma(request):
    datos = Cronograma.objects.all()
    return render(request, "Cronograma.html",{"datos":datos})


def exit(request):
    logout(request)
    return redirect('Home')

from os import remove, path

from django.shortcuts import render, reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import FileForm, EditForm
from .models import UploadedFiles
from .afd import AFD


def index(request):
    return HttpResponse('este es el index')

def home(request):
    return render(request, 'registro/home.html', context=None)

def actualizar_datos(request, nom):
    #definimos contexto para actualizar datos del que ya estaba loggeado
    user = User.objects.get(username=nom)
    conte = {'email': user.email, 'nombre': user.username, 'cui': user.profile.cui}
    return render(request, 'registro/editar_datos.html', context=conte)

def profile(request, nom):
    try:
        user = User.objects.get(username=nom)
        ctx = {'nombre': user.username, 'email': user.email, 'cui': user.profile.cui, 'profesion': user.profile.profesion}
        return render(request, 'registro/profile.html', context=ctx)
    except User.DoesNotExist:
        raise Http404('not found')

def create(request):
    return HttpResponse('este es el create')

def logged_out(request):
    return render(request, 'registration/salir.html', context = None)

def editar(request):
    return HttpResponse('aca deberia ir el formulario para cambiar datos')

def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(True, request.user)

            return HttpResponseRedirect(reverse('files list'))
    else:
        form = FileForm
    return render(request, 'main/file_uploaded.html', {'form':form })

def files_list(request):
    files = UploadedFiles.objects.filter(user=request.user)
    return render(request, 'main/files_list.html', {'files':files})


def edicion(request, id_archivo):
    upload = UploadedFiles.objects.get(pk=id_archivo)
    file = upload.p2.open('rt')
    contenido = file.read()
    file.close()
    afd = AFD(request.user.profile.profesion)
    colorizado = afd.colorizar(contenido)

    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            upload.title = form.cleaned_data.get('title')
            if path.isfile(upload.p2.path):
                remove(upload.p2.path)

            with open(upload.p2.path, 'wt') as destination:
                destination.write(form.cleaned_data.get('contenido'))
    else:
        nombre = upload.title
        form = EditForm(initial={'title': nombre, 'contenido':contenido})

    return render(request, 'main/edicion.html', context={'form':form, 'colorizado':colorizado})
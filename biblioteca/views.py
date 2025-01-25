from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import LivroCreationForm
from .models import Livro

# Create your views here.
def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def livros(request):
    template = loader.get_template('livros.html')
    context = {
        'livros': Livro.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def livro_detalhes(request, id):
    livro = Livro.objects.get(id=id)
    template = loader.get_template('livro_detalhes.html')
    context = {
        'livro': livro,
    }
    return HttpResponse(template.render(context, request))

def livro_cadastro(request):
    if request.method == 'POST':
        form = LivroCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros')
        else: print(form.errors)
    else:
        form = LivroCreationForm()
    return render(request, 'cadastro_livro.html', {'form': form})

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('principal')
        else: print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # por causa daqui
            if user is not None:
                login(request, user)
                return redirect('principal')
        else:
            print(form)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
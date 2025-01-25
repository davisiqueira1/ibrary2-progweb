from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LivroCreationForm
from .models import Livro, Emprestimo
from django.utils.timezone import now
from datetime import timedelta

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

def livro_excluir(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('livros')

def livro_editar(request, id):
    livro = Livro.objects.get(id=id)
    if request.method == 'POST':
        form = LivroCreationForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livros')
        else: print(form.errors)
    else:
        form = LivroCreationForm(instance=livro)

    return render(request, 'livro_editar.html', {'form': form, 'livro': livro})

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

def emprestimos(request):
    template = loader.get_template('emprestimos.html')
    emprestimos = Emprestimo.objects.filter(usuario=request.user)
    context = {
        'emprestimos': emprestimos,
    }
    return HttpResponse(template.render(context, request))

def emprestimo_cancelar(request, id):
    emprestimo = Emprestimo.objects.get(id=id)
    emprestimo.delete()
    return redirect('emprestimos')

def emprestimo_estender(request, id):
    emprestimo = Emprestimo.objects.get(id=id)
    emprestimo.data_devolucao = emprestimo.data_devolucao + timedelta(days=7)
    emprestimo.save()

    template = loader.get_template('emprestimo_detalhes.html')
    context = {
        'emprestimo': emprestimo,
    }
    return HttpResponse(template.render(context, request))

def emprestimo_detalhes(request, id):
    emprestimo = Emprestimo.objects.get(id=id)
    template = loader.get_template('emprestimo_detalhes.html')
    context = {
        'emprestimo': emprestimo,
    }
    return HttpResponse(template.render(context, request))

@login_required
def emprestimo_cadastrar(request, id):
    livro = get_object_or_404(Livro, id=id)
    emprestimo = Emprestimo.objects.create(
        livro=livro,
        usuario=request.user,
        data_emprestimo=now(),
        data_devolucao=now() + timedelta(days=7),
    )
    emprestimo.save()
    return redirect("emprestimos")

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
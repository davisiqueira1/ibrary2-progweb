from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UsuarioCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def livros(request):
    template = loader.get_template('livros.html')
    context = {
        'livros': [
            {'id': 1, 'titulo': 'Dom Casmurro',  'autor': 'Machado de Assis'},
            {'id': 2,'titulo': 'O Cortiço',  'autor': 'Aluísio Azevedo'},
            {'id':3,'titulo': 'Memórias Póstumas de Brás Cubas',  'autor': 'Machado de Assis'},
            {'id':4,'titulo': 'A Moreninha',  'autor': 'Joaquim Manuel de Macedo'},
            {'id':5,'titulo': 'O Guarani',  'autor': 'José de Alencar'},
            {'id':6,'titulo': 'Iracema',  'autor': 'José de Alencar'},
            {'id':7,'titulo': 'O Alienista',  'autor': 'Machado de Assis'},
            {'id':8,'titulo': 'O Primo Basílio',  'autor': 'Eça de Queirós'},
            {'id':9,'titulo': 'O Mulato',  'autor': 'Aluísio Azevedo'},
            {'id':10,'titulo': 'O Ateneu',  'autor': 'Raul Pompeia'},
        ]
    }
    return HttpResponse(template.render(context, request))

def livro_detalhes(request, id):
    livros = [
            {'id': 1, 'titulo': 'Dom Casmurro',  'autor': 'Machado de Assis'},
            {'id': 2,'titulo': 'O Cortiço',  'autor': 'Aluísio Azevedo'},
            {'id':3,'titulo': 'Memórias Póstumas de Brás Cubas',  'autor': 'Machado de Assis'},
            {'id':4,'titulo': 'A Moreninha',  'autor': 'Joaquim Manuel de Macedo'},
            {'id':5,'titulo': 'O Guarani',  'autor': 'José de Alencar'},
            {'id':6,'titulo': 'Iracema',  'autor': 'José de Alencar'},
            {'id':7,'titulo': 'O Alienista',  'autor': 'Machado de Assis'},
            {'id':8,'titulo': 'O Primo Basílio',  'autor': 'Eça de Queirós'},
            {'id':9,'titulo': 'O Mulato',  'autor': 'Aluísio Azevedo'},
            {'id':10,'titulo': 'O Ateneu',  'autor': 'Raul Pompeia'},
    ]
    livro = livros[id-1]
    template = loader.get_template('livro_detalhes.html')
    context = {
        'livro': livro,
    }
    return HttpResponse(template.render(context, request))

# cadastro cria um registro do biblioteca.Usuario, não do user padrão
def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('principal')
    else:
        form = UsuarioCreationForm()
    return render(request, 'cadastro.html', {'form': form})

# login funcionando pro user padrão do django, mas não pro biblioteca.Usuario
# de resto funciona 100% (se testar com admin/admin, por exemplo)
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
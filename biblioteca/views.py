from django.http import HttpResponse
from django.template import loader

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
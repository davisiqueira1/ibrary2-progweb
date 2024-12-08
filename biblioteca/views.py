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
            {'titulo': 'Dom Casmurro',  'autor': 'Machado de Assis'},
            {'titulo': 'O Cortiço',  'autor': 'Aluísio Azevedo'},
            {'titulo': 'Memórias Póstumas de Brás Cubas',  'autor': 'Machado de Assis'},
            {'titulo': 'A Moreninha',  'autor': 'Joaquim Manuel de Macedo'},
            {'titulo': 'O Guarani',  'autor': 'José de Alencar'},
            {'titulo': 'Iracema',  'autor': 'José de Alencar'},
            {'titulo': 'O Alienista',  'autor': 'Machado de Assis'},
            {'titulo': 'O Primo Basílio',  'autor': 'Eça de Queirós'},
            {'titulo': 'O Mulato',  'autor': 'Aluísio Azevedo'},
            {'titulo': 'O Ateneu',  'autor': 'Raul Pompeia'},
        ]
    }
    return HttpResponse(template.render(context, request))
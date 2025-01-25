from django import forms
from .models import Livro

class LivroCreationForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'descricao', 'genero', 'isbn']
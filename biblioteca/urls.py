from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('livros', views.livros, name='livros'),
    path('livros/cadastro', views.livro_cadastro, name='livros_cadastro'),
    path('livros/detalhes/<int:id>', views.livro_detalhes, name='livro_detalhes'),
    path('livros/excluir/<int:id>', views.livro_excluir, name='livro_excluir'),
    path('livros/editar/<int:id>', views.livro_editar, name='livro_editar'),
    path('auth/cadastro/', views.cadastro, name='cadastro'),
    path('auth/login', views.login_view, name='login')
]
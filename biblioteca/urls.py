from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('livros', views.livros, name='livros'),
    path('livros/cadastro', views.livro_cadastro, name='livros_cadastro'),
    path('livros/detalhes/<int:id>', views.livro_detalhes, name='livro_detalhes'),
    path('livros/excluir/<int:id>', views.livro_excluir, name='livro_excluir'),
    path('livros/editar/<int:id>', views.livro_editar, name='livro_editar'),
    path('auth/cadastro/', views.cadastro, name='cadastro'),
    path('auth/login', views.login_view, name='login'),
    path('auth/logout', views.logout_view, name='logout'),
    path('emprestimos', views.emprestimos, name='emprestimos'),
    path('emprestimos/cadastro/<int:id>', views.emprestimo_cadastrar, name='emprestimo_cadastrar'),
    path('emprestimos/detalhes/<int:id>', views.emprestimo_detalhes, name='emprestimo_detalhes'),
    path('emprestimos/cancelar/<int:id>', views.emprestimo_cancelar, name='emprestimo_cancelar'),
    path('emprestimos/estender/<int:id>', views.emprestimo_estender, name='emprestimo_estender'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('livros', views.livros, name='livros'),
    path('livros/detalhes/<int:id>', views.livro_detalhes, name='livro_detalhes')
]
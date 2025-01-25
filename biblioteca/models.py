from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class UsuarioManager(BaseUserManager):
    def create_user(self, nome, password=None, admin=False):
        if not nome:
            raise ValueError('O nome do usuário deve ser fornecido')
        user = self.model(nome=nome, admin=admin)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, password=None):
        user = self.create_user(nome, password=password, admin=True)
        user.save(using=self._db)
        return user

class Emprestimo(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='emprestimos'
    )
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='emprestimos'
    )
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.usuario.nome} - {self.livro.nome}'

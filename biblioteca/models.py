from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nome'

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin

class Emprestimo(models.Model):
    usuario = models.ForeignKey(
        Usuario,
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

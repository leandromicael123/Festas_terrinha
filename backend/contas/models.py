from django.conf import settings
from django.db import models


class Interesse(models.Model):
    nome = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nome


class PerfilUtilizador(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="perfil")
    nome_publico = models.CharField(max_length=120)
    fotografia = models.ImageField(upload_to="perfis/", blank=True)
    biografia = models.TextField(blank=True)
    localidade_preferida = models.CharField(max_length=120, blank=True)
    interesses = models.ManyToManyField(Interesse, blank=True)
    organizador_validado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_publico

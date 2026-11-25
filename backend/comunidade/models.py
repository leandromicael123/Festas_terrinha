from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


NOTAS = [MinValueValidator(1), MaxValueValidator(5)]


class Avaliacao(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edicao = models.ForeignKey("catalogo.EdicaoFesta", on_delete=models.CASCADE, related_name="avaliacoes")
    estrelas_globais = models.PositiveSmallIntegerField(validators=NOTAS)
    musica = models.PositiveSmallIntegerField(null=True, blank=True, validators=NOTAS)
    gastronomia = models.PositiveSmallIntegerField(null=True, blank=True, validators=NOTAS)
    precos = models.PositiveSmallIntegerField(null=True, blank=True, validators=NOTAS)
    organizacao = models.PositiveSmallIntegerField(null=True, blank=True, validators=NOTAS)
    acessos = models.PositiveSmallIntegerField(null=True, blank=True, validators=NOTAS)
    etiquetas = models.JSONField(default=list, blank=True)
    comentario = models.TextField(blank=True)
    fotografia = models.ImageField(upload_to="avaliacoes/", blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(estrelas_globais__range=(1, 5)), name="avaliacao_global_1_a_5"),
        ]


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edicao = models.ForeignKey("catalogo.EdicaoFesta", on_delete=models.CASCADE, related_name="publicacoes")
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


class MediaPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="fotos")
    fotografia = models.ImageField(upload_to="publicacoes/")


class ComentarioPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="gostos")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["post", "user"], name="gosto_unico_por_conta")]


class Favorito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favoritos")
    edicao = models.ForeignKey("catalogo.EdicaoFesta", on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "edicao"], name="favorito_unico_por_conta")]

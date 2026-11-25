from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Festa(models.Model):
    nome = models.CharField(max_length=160)
    localidade = models.CharField(max_length=120)
    concelho = models.CharField(max_length=120)
    distrito = models.CharField(max_length=120)
    categoria = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class EdicaoFesta(models.Model):
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE, related_name="edicoes")
    organizador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="edicoes_organizadas")
    ano = models.PositiveSmallIntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    recinto = models.CharField(max_length=180)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    preco = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    aprovada = models.BooleanField(default=False)

    class Meta:
        ordering = ["data_inicio", "pk"]
        constraints = [
            models.CheckConstraint(condition=models.Q(data_fim__gte=models.F("data_inicio")), name="edicao_datas_validas"),
            models.CheckConstraint(condition=models.Q(preco__gte=0), name="edicao_preco_valido"),
        ]

    def __str__(self):
        return f"{self.festa} ({self.ano})"


class ItemCartaz(models.Model):
    edicao = models.ForeignKey(EdicaoFesta, on_delete=models.CASCADE, related_name="cartaz")
    artista = models.CharField(max_length=160, blank=True)
    atividade = models.CharField(max_length=180)
    inicio = models.DateTimeField()

    class Meta:
        ordering = ["inicio", "pk"]


class MediaEdicao(models.Model):
    edicao = models.ForeignKey(EdicaoFesta, on_delete=models.CASCADE, related_name="multimedia")
    fotografia = models.ImageField(upload_to="edicoes/", blank=True)
    video_url = models.URLField(blank=True)

from io import StringIO

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.db import IntegrityError, connection, transaction
from django.test import TestCase

from catalogo.models import EdicaoFesta
from .models import Avaliacao, Favorito, LikePost, Post


class RelacoesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("carregar_demo", stdout=StringIO())
        cls.user = get_user_model().objects.create_user("participante")
        cls.edicao = EdicaoFesta.objects.first()

    def test_fk_de_conta_e_edicao_na_mesma_base(self):
        with connection.cursor() as cursor:
            for model in (Avaliacao, Post, Favorito):
                constraints = connection.introspection.get_constraints(cursor, model._meta.db_table)
                targets = {entry["foreign_key"] for entry in constraints.values() if entry["foreign_key"]}
                self.assertIn((get_user_model()._meta.db_table, "id"), targets)
                self.assertIn((EdicaoFesta._meta.db_table, "id"), targets)

    def test_favorito_e_gosto_sao_unicos_por_conta(self):
        post = Post.objects.create(edicao=self.edicao, user=self.user, texto="Teste")
        for model, fields in [(Favorito, {"edicao": self.edicao}), (LikePost, {"post": post})]:
            model.objects.create(user=self.user, **fields)
            with self.assertRaises(IntegrityError), transaction.atomic():
                model.objects.create(user=self.user, **fields)

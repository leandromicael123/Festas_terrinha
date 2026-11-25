from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from .models import EdicaoFesta, ItemCartaz


class CatalogoBaseTests(TestCase):
    def setUp(self):
        call_command("carregar_demo", stdout=StringIO())

    def test_demo_repetida_preserva_dados(self):
        edicao = EdicaoFesta.objects.first()
        edicao.recinto = "Recinto atualizado"
        edicao.save()
        call_command("carregar_demo", stdout=StringIO())
        edicao.refresh_from_db()
        self.assertEqual(edicao.recinto, "Recinto atualizado")
        self.assertEqual(EdicaoFesta.objects.count(), 2)
        self.assertEqual(ItemCartaz.objects.count(), 2)

    def test_lista_e_detalhe_mostram_apenas_edicoes_aprovadas(self):
        visivel, pendente = EdicaoFesta.objects.all()
        pendente.aprovada = False
        pendente.save()
        base = "/api/catalogo/edicoes/"
        lista = self.client.get(base).json()
        self.assertEqual([r["id"] for r in lista], [visivel.pk])
        self.assertEqual(self.client.get(f"{base}{visivel.pk}/").json(), lista[0])
        self.assertEqual(self.client.get(f"{base}{pendente.pk}/").status_code, 404)
        self.assertIsInstance(lista[0]["latitude"], float)

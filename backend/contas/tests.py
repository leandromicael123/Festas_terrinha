import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase


class SessaoTests(TestCase):
    def test_login_exige_csrf_e_logout_termina_sessao(self):
        user = get_user_model().objects.create_user("teste", password="apenas-para-este-teste")
        client = Client(enforce_csrf_checks=True)
        url = "/api/contas/sessao/"
        inicial = client.get(url).json()
        self.assertIsNone(inicial["user"])
        dados = {"username": user.username, "password": "apenas-para-este-teste"}
        self.assertEqual(client.post(url, dados, content_type="application/json").status_code, 403)
        sessao = client.post(
            url, dados, content_type="application/json", HTTP_X_CSRFTOKEN=inicial["csrfToken"]
        ).json()
        self.assertEqual(sessao["user"]["id"], user.pk)
        self.assertEqual(client.get(url).json()["user"]["id"], user.pk)
        self.assertNotEqual(sessao["csrfToken"], inicial["csrfToken"])
        self.assertIsNone(client.delete(url, HTTP_X_CSRFTOKEN=sessao["csrfToken"]).json()["user"])

    def test_pedido_invalido_e_credenciais_erradas(self):
        url = "/api/contas/sessao/"
        self.assertEqual(self.client.post(url, json.dumps([]), content_type="application/json").status_code, 400)
        resposta = self.client.post(url, {"username": "inexistente", "password": "teste"}, content_type="application/json")
        self.assertEqual(resposta.status_code, 401)

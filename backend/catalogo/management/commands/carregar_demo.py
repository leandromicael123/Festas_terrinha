from datetime import date, datetime
from zoneinfo import ZoneInfo

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from catalogo.models import EdicaoFesta, Festa, ItemCartaz
from contas.models import PerfilUtilizador


class Command(BaseCommand):
    help = "Acrescenta duas edições fictícias para desenvolvimento local."

    @transaction.atomic
    def handle(self, *args, **options):
        user, created = get_user_model().objects.get_or_create(
            username="organizador_demo", defaults={"is_active": False}
        )
        if created:
            user.set_unusable_password()
            user.save(update_fields=["password"])
        elif user.is_active or user.has_usable_password():
            raise CommandError("O nome organizador_demo já pertence a uma conta com acesso.")
        PerfilUtilizador.objects.get_or_create(
            user=user, defaults={"nome_publico": "Organização de demonstração", "organizador_validado": True}
        )
        exemplos = [
            ("Arraial do Largo", "Lisboa", "Alfama", "Arraial", 12, "Largo do Chafariz", "38.711600", "-9.129500", "0.00"),
            ("Romaria do Norte", "Porto", "Miragaia", "Romaria", 23, "Largo da Ribeira", "41.141200", "-8.616300", "5.00"),
        ]
        for nome, cidade, local, categoria, dia, recinto, lat, lon, preco in exemplos:
            festa, _ = Festa.objects.get_or_create(
                nome=nome, localidade=local,
                defaults={"distrito": cidade, "concelho": cidade, "categoria": categoria},
            )
            edicao, _ = EdicaoFesta.objects.get_or_create(
                festa=festa, ano=2027, organizador=user,
                defaults={
                    "data_inicio": date(2027, 6, dia), "data_fim": date(2027, 6, dia + 1),
                    "recinto": recinto, "latitude": lat, "longitude": lon, "preco": preco, "aprovada": True,
                },
            )
            ItemCartaz.objects.get_or_create(
                edicao=edicao, atividade="Concerto de abertura",
                defaults={"artista": "Banda do Largo", "inicio": datetime(2027, 6, dia, 21, tzinfo=ZoneInfo("Europe/Lisbon"))},
            )
        self.stdout.write(self.style.SUCCESS("Dados de demonstração disponíveis."))

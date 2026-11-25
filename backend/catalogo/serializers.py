from rest_framework import serializers

from .models import EdicaoFesta


class EdicaoSerializer(serializers.ModelSerializer):
    nome_festa = serializers.CharField(source="festa.nome", read_only=True)
    localidade = serializers.CharField(source="festa.localidade", read_only=True)
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)

    class Meta:
        model = EdicaoFesta
        fields = (
            "id", "festa", "nome_festa", "localidade", "organizador", "ano",
            "data_inicio", "data_fim", "recinto", "latitude", "longitude", "preco", "aprovada",
        )

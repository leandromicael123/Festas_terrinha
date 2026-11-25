from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import EdicaoFesta
from .serializers import EdicaoSerializer


class EdicaoPublicaViewSet(ReadOnlyModelViewSet):
    queryset = EdicaoFesta.objects.filter(aprovada=True).select_related("festa")
    serializer_class = EdicaoSerializer
    permission_classes = [AllowAny]

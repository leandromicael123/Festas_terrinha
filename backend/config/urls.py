from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from catalogo.views import EdicaoPublicaViewSet
from contas.views import sessao

router = SimpleRouter()
router.register("edicoes", EdicaoPublicaViewSet, basename="edicao")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/contas/sessao/", sessao),
    path("api/catalogo/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

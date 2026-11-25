from django.contrib import admin

from .models import Interesse, PerfilUtilizador

admin.site.register([Interesse, PerfilUtilizador])

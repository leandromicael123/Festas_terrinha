from django.contrib import admin

from .models import EdicaoFesta, Festa, ItemCartaz, MediaEdicao

admin.site.register([Festa, EdicaoFesta, ItemCartaz, MediaEdicao])

from django.contrib import admin

from .models import Avaliacao, ComentarioPost, Favorito, LikePost, MediaPost, Post

admin.site.register([Avaliacao, Post, MediaPost, ComentarioPost, LikePost, Favorito])

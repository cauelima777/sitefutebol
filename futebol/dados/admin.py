# admin.py

from django.contrib import admin
from .models import Jogador, Dados

admin.site.register(Jogador)
admin.site.register(Dados)

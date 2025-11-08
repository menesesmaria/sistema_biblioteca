from django.contrib import admin
from .models import Livro, Editora  # ou os modelos que estiverem nesse app

admin.site.register(Livro)
admin.site.register(Editora)

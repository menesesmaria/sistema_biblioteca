from django.contrib import admin
from .models import Estado, Cidade, Bairro, Logradouro

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Logradouro)

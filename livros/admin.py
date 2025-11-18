from django.contrib import admin
from .models import Editora, EntidadeProprietaria, Autor, GeneroObra, TipoObra, Livro, Exemplar

admin.site.register(Editora)
admin.site.register(EntidadeProprietaria)
admin.site.register(Autor)
admin.site.register(GeneroObra)
admin.site.register(TipoObra)
admin.site.register(Livro)
admin.site.register(Exemplar)

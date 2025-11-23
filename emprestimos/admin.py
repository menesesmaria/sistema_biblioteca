from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):

    @admin.display(description="Valor da multa")
    def valor_multa_reais(self, obj):
        return f"R$ {obj.valor_multa:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


    list_display = ['usuario', 'exemplar', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao', 'status', 'valor_multa_reais']

    list_filter = ('status',)

    list_per_page = 20

    list_select_related = ('usuario', 'exemplar')


from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'exemplar', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao', 'status', 'valor_multa_reais', 'multa_paga']
    list_filter = ('status', 'multa_paga')

    @admin.display(description="Valor da multa")
    def valor_multa_reais(self, obj):
        return f"R$ {obj.valor_multa:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


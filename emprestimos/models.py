from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta, date
from usuarios.models import Usuario
from livros.models import Exemplar


class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario')
    exemplar = models.ForeignKey(Exemplar, models.DO_NOTHING, db_column='exemplar')
    data_emprestimo = models.DateField()
    data_devolucao_prevista = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30, default="Emprestado")

    multa_por_dia = 2  

    class Meta:
        managed = False
        db_table = 'emprestimo'

    def clean(self):
        """Impedir empréstimo duplicado."""
        if not self.pk:
            ja_emprestado = Emprestimo.objects.filter(
                exemplar=self.exemplar,
                data_devolucao__isnull=True
            ).exists()

            if ja_emprestado:
                raise ValidationError(
                    "Este exemplar já está emprestado e ainda não foi devolvido."
                )

    def save(self, *args, **kwargs):
        if not self.data_devolucao_prevista:
            self.data_devolucao_prevista = self.data_emprestimo + timedelta(days=7)

        if self.data_devolucao:
            if self.data_devolucao > self.data_devolucao_prevista:
                self.status = "Devolvido com atraso"
            else:
                self.status = "Devolvido"

        else:
            hoje = date.today()
            if hoje > self.data_devolucao_prevista:
                self.status = "Atrasado"
            else:
                self.status = "Emprestado"

        super().save(*args, **kwargs)


    @property
    def atrasado(self):
        """Retorna True se o empréstimo está atrasado."""
        hoje = date.today()

        if self.data_devolucao:
            return self.data_devolucao > self.data_devolucao_prevista

        return hoje > self.data_devolucao_prevista

    @property
    def dias_atraso(self):
        """Dias de atraso."""
        if not self.atrasado:
            return 0

        fim = self.data_devolucao or date.today()
        return (fim - self.data_devolucao_prevista).days

    @property
    def valor_multa(self):
        """Valor da multa calculada."""
        return self.dias_atraso * self.multa_por_dia

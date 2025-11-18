from django.db import models
from usuarios.models import Usuario
from livros.models import Exemplar


# Create your models here.

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario')
    exemplar = models.ForeignKey(Exemplar, models.DO_NOTHING, db_column='exemplar')
    data_emprestimo = models.DateField()
    data_devolucao_prevista = models.DateField()
    data_devolucao = models.DateField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'emprestimo'

class Atraso(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, models.DO_NOTHING, db_column='emprestimo')
    valor_multa = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=150)
    data_devolucao_prevista = models.DateField()

    class Meta:
        managed = False
        db_table = 'atraso'


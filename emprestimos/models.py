from django.db import models
from usuarios.models import Usuario
from livros.models import Exemplar


# Create your models here.

class Emprestimo(models.Model):
    idemprestimo = models.AutoField(db_column='idEmprestimo', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idexemplar = models.ForeignKey(Exemplar, models.DO_NOTHING, db_column='idExemplar')  # Field name made lowercase.
    dataemprestimo = models.DateField(db_column='dataEmprestimo')  # Field name made lowercase.
    datadevolucaoprevista = models.DateField(db_column='dataDevolucaoPrevista')  # Field name made lowercase.
    datadevolucao = models.DateField(db_column='dataDevolucao')  # Field name made lowercase.
    status = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.idusuario} - {self.idexemplar} - {self.status}"

    class Meta:
        managed = False
        db_table = 'emprestimo'

class Atraso(models.Model):
    idatraso = models.AutoField(db_column='idAtraso', primary_key=True)  # Field name made lowercase.
    idemprestimo = models.ForeignKey(Emprestimo, models.DO_NOTHING, db_column='idEmprestimo')  # Field name made lowercase.
    valormulta = models.DecimalField(db_column='valorMulta', max_digits=10, decimal_places=0)  # Field name made lowercase.
    status = models.CharField(max_length=6)
    datadevolucaoprevista = models.DateField(db_column='dataDevolucaoPrevista')  # Field name made lowercase.

    def __str__(self):
        return f"{self.idemprestimo} - {self.status}"

    class Meta:
        managed = False
        db_table = 'atraso'


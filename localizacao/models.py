from django.db import models

# Create your models here.

class Bairro(models.Model):
    idbairro = models.AutoField(db_column='idBairro', primary_key=True)  # Field name made lowercase.
    idcidade = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='idCidade')  # Field name made lowercase.
    bairro = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'bairro'


class Cidade(models.Model):
    idcidade = models.AutoField(db_column='idCidade', primary_key=True)  # Field name made lowercase.
    idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='idEstado')  # Field name made lowercase.
    cidade = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cidade'


class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'estado'


class Logradouro(models.Model):
    idlogradouro = models.AutoField(db_column='idLogradouro', primary_key=True)  # Field name made lowercase.
    idbairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='idBairro')  # Field name made lowercase.
    tipo = models.CharField(max_length=9)
    nome = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'logradouro'


from django.db import models

# Create your models here.

class Estado(models.Model):
    estado = models.CharField(max_length=150)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'estado'

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado')
    cidade = models.CharField(max_length=150)
    
    class Meta:
        managed = False
        db_table = 'cidade'


class Bairro(models.Model):
    id_cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='id_cidade')
    bairro = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'bairro'

class Logradouro(models.Model):
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='bairro')
    tipo = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'logradouro'
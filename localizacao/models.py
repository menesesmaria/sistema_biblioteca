from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Estado(models.Model):
    estado = models.CharField(max_length=150)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'estado'
    
    def __str__(self):
        return f"{self.estado}/{self.sigla}"

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado')
    cidade = models.CharField(max_length=150)
    
    class Meta:
        managed = False
        db_table = 'cidade'

    def __str__(self):
        return f"{self.cidade}"


class Bairro(models.Model):
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='cidade')
    bairro = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'bairro'
    
    def __str__(self):
        return f"{self.bairro}"
    
class tipoLogradouro(models.TextChoices):
    rua = 'Rua'
    avenida = 'Avenida'
    praça = 'Praça'
    travessa = 'Travessa'
    vielas = 'Viela'
    rodovias = 'Rodovias'
    alameda = 'Alameda'
    ladeira= 'Ladeira'
    

class Logradouro(models.Model):
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='bairro')
    tipo = models.CharField(max_length=30, choices=tipoLogradouro.choices)
    nome = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'logradouro'

    def __str__(self):
        return f"{self.tipo} {self.nome}"
from django.db import models
from localizacao.models import Bairro, Cidade, Estado, Logradouro

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado')
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='cidade')
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='bairro')
    logradouro = models.ForeignKey(Logradouro, models.DO_NOTHING, db_column='logradouro')
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'

from django.db import models
from localizacao.models import Bairro, Cidade, Estado, Logradouro
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=30, unique=True)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado')
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado')
    cidade = ChainedForeignKey(
        Cidade,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.DO_NOTHING,
        db_column='cidade'
    )
    bairro = ChainedForeignKey(
        Bairro,
        chained_field="cidade",
        chained_model_field="cidade",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.DO_NOTHING,
        db_column='bairro'
    )
    logradouro = ChainedForeignKey(
        Logradouro,
        chained_field="bairro",
        chained_model_field="bairro",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.DO_NOTHING,
        db_column='logradouro'
    )
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nome}"

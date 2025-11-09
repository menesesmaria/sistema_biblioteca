from django.db import models
from localizacao.models import Bairro, Cidade, Estado, Logradouro

# Create your models here.

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nome = models.IntegerField()
    datanascimento = models.DateField(db_column='dataNascimento')  # Field name made lowercase.
    cpf = models.IntegerField(db_comment='somente n·meros')
    telefone = models.IntegerField(db_comment='somente n·meros')
    email = models.CharField(max_length=30)
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='idEstado')  # Field name made lowercase.
    idcidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='idCidade')  # Field name made lowercase.
    idbairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='idBairro')  # Field name made lowercase.
    idlogradouro = models.ForeignKey(Logradouro, models.DO_NOTHING, db_column='idLogradouro')  # Field name made lowercase.
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'

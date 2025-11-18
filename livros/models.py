from django.db import models
from localizacao.models import Bairro, Cidade, Estado, Logradouro

# Create your models here.

class Editora(models.Model):
    editora = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15, db_comment='somente n·meros')
    email = models.CharField(max_length=30)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado')
    cidade = ChainedForeignKey (
        Cidade,
        chained_field="idestado",
        chained_model_field="idestado",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.DO_NOTHING,
        db_column='cidade'
    )
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='bairro')
    logradouro = models.ForeignKey(Logradouro, models.DO_NOTHING, db_column='logradouro')
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editora'
        

class EntidadeProprietaria(models.Model):
    entidade = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado')
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='cidade')
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='bairro')
    logradouro = models.ForeignKey(Logradouro, models.DO_NOTHING, db_column='logradouro')
    numero = models.IntegerField()
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'entidade_proprietaria'

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    nome_meio = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'autor'

class GeneroObra(models.Model):
    genero = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'genero_obra'

class TipoObra(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tipo_obra'

class Livro(models.Model):
    livro = models.CharField(max_length=150)
    volume = models.IntegerField()
    autor = models.ForeignKey(Autor, models.DO_NOTHING, db_column='autor')
    edicao = models.IntegerField()
    tipo = models.ForeignKey(TipoObra, models.DO_NOTHING, db_column='tipo')
    editora = models.ForeignKey(Editora, models.DO_NOTHING, db_column='editora')
    entidade = models.ForeignKey(EntidadeProprietaria, models.DO_NOTHING, db_column='entidade')
    isbn = models.CharField(max_length=15)
    genero = models.ForeignKey(GeneroObra, models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = False
        db_table = 'livro'

class Exemplar(models.Model):
    livro = models.ForeignKey(Livro, models.DO_NOTHING, db_column='livro')
    tombo = models.IntegerField()
    exemplar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exemplar'




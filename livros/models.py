from django.db import models
from localizacao.models import Bairro, Cidade, Estado, Logradouro

# Create your models here.

class Editora(models.Model):
    ideditora = models.AutoField(db_column='idEditora', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=30)
    cnpj = models.IntegerField(db_comment='somente n·meros')
    telefone = models.IntegerField(db_comment='somente n·meros')
    email = models.CharField(max_length=30)
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='idEstado')  # Field name made lowercase.
    idcidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='idCidade')  # Field name made lowercase.
    idbairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='idBairro')  # Field name made lowercase.
    idlogradouro = models.ForeignKey(Logradouro, models.DO_NOTHING, db_column='idLogradouro')  # Field name made lowercase.
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editora'
        

class EntidadeProprietaria(models.Model):
    identidade = models.AutoField(db_column='idEntidade', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=30)
    cnpj = models.IntegerField(db_comment='somente n·meros')
    telefone = models.IntegerField(db_comment='somente n·meros')
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='idEstado')  # Field name made lowercase.
    idcidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='idCidade')  # Field name made lowercase.
    idbairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='idBairro')  # Field name made lowercase.
    idlogradouro = models.ForeignKey(Logradouro, models.DO_NOTHING, db_column='idLogradouro')  # Field name made lowercase.
    numero = models.IntegerField()
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'entidade_proprietaria'

class Autor(models.Model):
    idautor = models.AutoField(db_column='idAutor', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=30)
    nomemeio = models.CharField(db_column='nomeMeio', max_length=30)  # Field name made lowercase.
    sobrenome = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'autor'

class GeneroObra(models.Model):
    idgenero = models.AutoField(db_column='idGenero', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'genero_obra'

class TipoObra(models.Model):
    idtipo = models.AutoField(db_column='idTipo', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tipo_obra'

class Livro(models.Model):
    idlivro = models.AutoField(db_column='idLivro', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=30)
    volume = models.IntegerField()
    idautor = models.ForeignKey(Autor, models.DO_NOTHING, db_column='idAutor')  # Field name made lowercase.
    edicao = models.IntegerField()
    idtipo = models.ForeignKey(TipoObra, models.DO_NOTHING, db_column='idTipo')  # Field name made lowercase.
    ideditora = models.ForeignKey(Editora, models.DO_NOTHING, db_column='idEditora')  # Field name made lowercase.
    identidade = models.ForeignKey(EntidadeProprietaria, models.DO_NOTHING, db_column='idEntidade')  # Field name made lowercase.
    isbn = models.IntegerField(db_comment='somente n·meors')
    idgenero = models.ForeignKey(GeneroObra, models.DO_NOTHING, db_column='idGenero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'livro'

class Exemplar(models.Model):
    idexemplar = models.AutoField(db_column='idExemplar', primary_key=True)  # Field name made lowercase.
    idlivro = models.ForeignKey(Livro, models.DO_NOTHING, db_column='idLivro')  # Field name made lowercase.
    tombo = models.IntegerField()
    exemplar = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'exemplar'




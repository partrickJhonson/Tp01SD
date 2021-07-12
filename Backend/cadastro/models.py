from django.db import models
from uuid import uuid4


class Cadastro(models.Model):
#Geral
    id_bidentificador = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    titulo = models.CharField(max_length=20,null=True)
    catalogo = models.CharField(max_length=20,null=True)
    EntradaNoCatalogo = models.DateField(auto_now_add=True)
    Lingua = models.CharField(max_length=20,null=True)
    Descrisao = models.CharField(max_length=20,null=True)
    palavrachave= models.CharField(max_length=20,null=True)
    Corbertura = models.CharField(max_length=20,null=True)
    Estrtura =  models.CharField(max_length=20,null=True)
    NiveldeAgregacao = models.IntegerField(default=0)
#Ciclo de Vida
    Versao = models.CharField(max_length=20,null=True)
    Status = models.CharField(max_length=10,null=True)
    ContribuinteFuncao = models.CharField(max_length=20,null=True)
    ContribuinteEntidadae = models.CharField(max_length=20,null=True)
    ContribuinteData = models.CharField(max_length=20,null=True)
#Meta-Metadados
    identificador = models.CharField(max_length=20,null=True)
    catalogoMeta = models.CharField(max_length=20,null=True)
    catalogoMetaEntrada = models.CharField(max_length=20,null=True)
    catalogoMetaData = models.CharField(max_length=20,null=True)
    EsquemaMeta = models.CharField(max_length=20,null=True)
    idiomameta = models.CharField(max_length=20,null=True)
#Tecnico
    formato = models.CharField(max_length=20,null=True)
    tamanho = models.CharField(max_length=20,null=True)
    localizacao = models.CharField(max_length=20,null=True)
    requisitoTipo = models.CharField(max_length=20,null=True)
    requisitoNome = models.CharField(max_length=20,null=True)
    Observacao= models.CharField(max_length=20,null=True)
    outrosRequitos = models.CharField(max_length=20,null=True)
    duracao = models.CharField(max_length=20,null=True)
#Educaional
    tipodeinteratividade = models.CharField(max_length=20,null=True)
    tipodeRecursodeAprendizagem = models.CharField(max_length=20,null=True)
    niveldeinteratividade = models.CharField(max_length=20,null=True)
    densidadesemantica = models.CharField(max_length=20,null=True)
    funcaodousuariofinalpretendido = models.CharField(max_length=20,null=True)
    contexto = models.CharField(max_length=20,null=True)
    faixaEtaria = models.CharField(max_length=20,null=True)
    dificuldade = models.CharField(max_length=20,null=True)
    TempodeAprendizagem = models.CharField(max_length=20,null=True)
    DescrisaoEducacional = models.CharField(max_length=20,null=True)
    idioma = models.CharField(max_length=20,null=True)
#Direitos
    custo = models.CharField(max_length=20,null=True)
    DireitosautoraisRestricoes = models.CharField(max_length=20,null=True)
    DescrisaoDireitos = models.CharField(max_length=20,null=True)
#Relacao
    tipoRelacao = models.CharField(max_length=20,null=True)
    recursoRelacao =models.CharField(max_length=20,null=True)
#Anotação
    pessoaAnotacao = models.CharField(max_length=20,null=True)
    dataanotacao = models.CharField(max_length=20,null=True)
    descrisaoanotacao = models.CharField(max_length=20,null=True)
#Clasificao
    closificacaoObjetivo = models.CharField(max_length=20,null=True)
    taxon = models.CharField(max_length=20,null=True)
    taxonFonte = models.CharField(max_length=20,null=True)
    taxonId = models.CharField(max_length=20,null=True)
    taxonEntrada = models.CharField(max_length=20,null=True)
    classificacaoDescrisao = models.CharField(max_length=20,null=True)
    PalavraPasseClassificacao = models.CharField(max_length=20,null=True)
    autor = models.CharField(max_length=20,null=True)
    ano_pulicacao = models.IntegerField(default=2020)
    estado = models.CharField(max_length=20,null=True)
    Npaginas = models.IntegerField(default=0)
    editora = models.CharField(max_length=20,null=True)
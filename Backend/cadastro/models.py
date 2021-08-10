from django.db import models
from uuid import uuid4


class Cadastro(models.Model):
    #Geral
    id_identificador = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    titulo = models.CharField(max_length=20)
    catalogo = models.CharField(max_length=20,null=True,blank=True)
    EntradaNoCatalogo = models.DateField(auto_now_add=True)
    Lingua = models.CharField(max_length=20,null=True,blank=True)
    Descrisao = models.CharField(max_length=20,null=True,blank=True)
    palavrachave= models.CharField(max_length=20,null=True,blank=True)
    Corbertura = models.CharField(max_length=20,null=True,blank=True)
    Estrtura =  models.CharField(max_length=20,null=True,blank=True)
    NiveldeAgregacao = models.IntegerField(default=0,null=True,blank=True)
#Ciclo de Vida
    Versao = models.CharField(max_length=20,null=True,blank=True)
    Status = models.CharField(max_length=10,null=True,blank=True)
    ContribuinteFuncao = models.CharField(max_length=20,null=True,blank=True)
    ContribuinteEntidadae = models.CharField(max_length=20,null=True,blank=True)
    ContribuinteData = models.CharField(max_length=20,null=True,blank=True)
#Meta-Metadados
    identificador = models.CharField(max_length=20,null=True,blank=True)
    catalogoMeta = models.CharField(max_length=20,null=True,blank=True)
    catalogoMetaEntrada = models.CharField(max_length=20,null=True,blank=True)
    catalogoMetaData = models.CharField(max_length=20,null=True,blank=True)
    EsquemaMeta = models.CharField(max_length=20,null=True,blank=True)
    idiomameta = models.CharField(max_length=20,null=True,blank=True)
#Tecnico
    formato = models.CharField(max_length=20,null=True,blank=True)
    tamanho = models.CharField(max_length=20,null=True,blank=True)
    localizacao = models.CharField(max_length=20,null=True,blank=True)
    requisitoTipo = models.CharField(max_length=20,null=True,blank=True)
    requisitoNome = models.CharField(max_length=20,null=True,blank=True)
    Observacao= models.CharField(max_length=20,null=True,blank=True)
    outrosRequitos = models.CharField(max_length=20,null=True,blank=True)
    duracao = models.CharField(max_length=20,null=True,blank=True)
#Educaional
    tipodeinteratividade = models.CharField(max_length=20,null=True,blank=True)
    tipodeRecursodeAprendizagem = models.CharField(max_length=20,null=True,blank=True)
    niveldeinteratividade = models.CharField(max_length=20,null=True,blank=True)
    densidadesemantica = models.CharField(max_length=20,null=True,blank=True)
    funcaodousuariofinalpretendido = models.CharField(max_length=20,null=True,blank=True)
    contexto = models.CharField(max_length=20,null=True,blank=True)
    faixaEtaria = models.CharField(max_length=20,null=True,blank=True)
    dificuldade = models.CharField(max_length=20,null=True,blank=True)
    TempodeAprendizagem = models.CharField(max_length=20,null=True,blank=True)
    DescrisaoEducacional = models.CharField(max_length=20,null=True,blank=True)
    idioma = models.CharField(max_length=20,null=True,blank=True)
#Direitos
    custo = models.CharField(max_length=20,null=True,blank=True)
    DireitosautoraisRestricoes = models.CharField(max_length=20,null=True,blank=True)
    DescrisaoDireitos = models.CharField(max_length=20,null=True,blank=True)
#Relacao
    tipoRelacao = models.CharField(max_length=20,null=True,blank=True)
    recursoRelacao =models.CharField(max_length=20,null=True,blank=True)
#Anotação
    pessoaAnotacao = models.CharField(max_length=20,null=True,blank=True)
    dataanotacao = models.CharField(max_length=20,null=True,blank=True)
    descrisaoanotacao = models.CharField(max_length=20,null=True,blank=True)
#Clasificao
    closificacaoObjetivo = models.CharField(max_length=20,null=True,blank=True)
    taxon = models.CharField(max_length=20,null=True,blank=True)
    taxonFonte = models.CharField(max_length=20,null=True,blank=True)
    taxonId = models.CharField(max_length=20,null=True,blank=True)
    taxonEntrada = models.CharField(max_length=20,null=True,blank=True)
    classificacaoDescrisao = models.CharField(max_length=20,null=True,blank=True)
    PalavraPasseClassificacao = models.CharField(max_length=20,null=True,blank=True)
    autor = models.CharField(max_length=20,null=True,blank=True)
    ano_pulicacao = models.IntegerField(default=2020)
    estado = models.CharField(max_length=20,null=True,blank=True)
    Npaginas = models.IntegerField(default=0,null=True,blank=True)
    editora = models.CharField(max_length=20,null=True,blank=True)


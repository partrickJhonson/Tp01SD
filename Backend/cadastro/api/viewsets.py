from rest_framework import viewsets
from cadastro.api import serializer
from cadastro import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class CadastroViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CadastroSerializer
    queryset = models.Cadastro.objects.all()
    filter_backends =[DjangoFilterBackend,OrderingFilter]
    ordering_fields = ['EntradaNoCatalogo']
  

class BuscarViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CadastroSerializer
    queryset = models.Cadastro.objects.all()
    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields= ['id_identificador','titulo','catalogo','Lingua','Descrisao','palavrachave','Corbertura','Estrtura','NiveldeAgregacao','Versao','Status','ContribuinteFuncao','ContribuinteEntidadae','ContribuinteData','identificador','catalogoMeta','catalogoMetaEntrada','catalogoMetaData','EsquemaMeta','idiomameta','formato','tamanho','localizacao','requisitoTipo','requisitoNome','Observacao','outrosRequitos','duracao','tipodeinteratividade','tipodeRecursodeAprendizagem','niveldeinteratividade','densidadesemantica','funcaodousuariofinalpretendido','contexto','faixaEtaria','dificuldade','TempodeAprendizagem','DescrisaoEducacional','idioma','custo','DireitosautoraisRestricoes','DescrisaoDireitos','tipoRelacao','recursoRelacao','pessoaAnotacao','dataanotacao','descrisaoanotacao','closificacaoObjetivo','taxon','taxonFonte','taxonId','taxonEntrada','classificacaoDescrisao','PalavraPasseClassificacao','autor','ano_pulicacao','estado','Npaginas','editora']
    search_fields =   ['id_identificador','titulo','catalogo','Lingua','Descrisao','palavrachave','Corbertura','Estrtura','NiveldeAgregacao','Versao','Status','ContribuinteFuncao','ContribuinteEntidadae','ContribuinteData','identificador','catalogoMeta','catalogoMetaEntrada','catalogoMetaData','EsquemaMeta','idiomameta','formato','tamanho','localizacao','requisitoTipo','requisitoNome','Observacao','outrosRequitos','duracao','tipodeinteratividade','tipodeRecursodeAprendizagem','niveldeinteratividade','densidadesemantica','funcaodousuariofinalpretendido','contexto','faixaEtaria','dificuldade','TempodeAprendizagem','DescrisaoEducacional','idioma','custo','DireitosautoraisRestricoes','DescrisaoDireitos','tipoRelacao','recursoRelacao','pessoaAnotacao','dataanotacao','descrisaoanotacao','closificacaoObjetivo','taxon','taxonFonte','taxonId','taxonEntrada','classificacaoDescrisao','PalavraPasseClassificacao','autor','ano_pulicacao','estado','Npaginas','editora']
    ordering_fields = ['EntradaNoCatalogo']
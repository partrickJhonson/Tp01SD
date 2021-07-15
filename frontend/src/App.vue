<!-- inicio da definição do templete da telas -->
<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="//" class="brand-logo center"> Cadastro de Metadados</a>
      </div>
    </nav>

    <div class="container">
      <form @submit.prevent="salvar">         
        <h2>Dados Gerais</h2>
        <hr>
        <label>Titulo</label>
        <input type="text" placeholder="Titulo"  v-model="objeto.titulo" >
        <label>Catalogo</label>
        <input type="text" placeholder="Caralogo" v-model="objeto.catalogo">

        <label>Língua</label>
        <input type="text" placeholder="Lingua" v-model="objeto.lingua">

        <label>Descrisão</label>
        <input type="text" placeholder="Descrisão" v-model="objeto.descrisao">

        <label>palavra Chave</label>
        <input type="text" placeholder="palavra chave" v-model="objeto.palavrachave">

        <label>Cobertura</label>
        <input type="text" placeholder="Cobertura" v-model="objeto.corbertura">

        <label>Estrtura</label>
        <input type="text" placeholder="Estrtura" v-model="objeto.estrtura">

        <label>Nivel de Agregação</label>
        <input type="text" placeholder="Nivel de Agregação" v-model="objeto.niveldeAgregacao">


        <h2>Ciclo de Vida</h2>
        <hr>
        <label>Versao</label>
        <input type="text" placeholder="Versao" v-model="objeto.Versao">

        <label>Status</label>
        <input type="text" placeholder="Status" v-model="objeto.Status">

        <label>Funcao do Contribuinte</label>
        <input type="text" placeholder="Funcao do Contribuinte" v-model="objeto.ContribuinteFuncao">

        <label>Entidada do Contribuinte</label>
        <input type="text" placeholder="Entidada do Contribuinte" v-model="objeto.ContribuinteEntidadae">

        <label>Data da  Contribuição</label>
        <input type="text" placeholder="Data da  Contribuição" v-model="objeto.ContribuinteData">

        <h2>Meta-Metadados</h2>
        <hr>
        <label>identificador</label>
        <input type="text" placeholder="identificador" v-model="objeto.identificador">

        <label>Catalogo</label>
        <input type="text" placeholder="Catalogo" v-model="objeto.catalogoMeta">

        <label>Catalogo de Entrada</label>
        <input type="text" placeholder="catalogo de Entrada" v-model="objeto.catalogoMetaEntrada">

        <label>Data Entrada</label>
        <input type="text" placeholder="Data Entrada" v-model="objeto.catalogoMetaData">

        <label>Esquema</label>
        <input type="text" placeholder="Esquema" v-model="objeto.EsquemaMeta">

        <label>Idioma</label>
        <input type="text" placeholder="Idioma" v-model="objeto.idiomameta">

        <h2>Técnico</h2>
        <hr>
        <label>formato</label>
        <input type="text" placeholder="formato" v-model="objeto.formato">

        <label>Tamanho</label>
        <input type="text" placeholder="tamanho" v-model="objeto.tamanho">

        <label>Localização</label>
        <input type="text" placeholder="Localização" v-model="objeto.localizacao">

        <label>Tipo de Requisito</label>
        <input type="text" placeholder="Tipo de Requisito" v-model="objeto.requisitoTipo">

        <label>Nome do Requisito</label>
        <input type="text" placeholder="Nome do Requisito" v-model="objeto.requisitoNome">

        <label>Observação</label>
        <input type="text" placeholder="Observação" v-model="objeto.Observacao">

        <label>Outros Requitos</label>
        <input type="text" placeholder="Outros Requisitos" v-model="objeto.outrosRequitos">

        <label>duracao</label>
        <input type="text" placeholder="duracao" v-model="objeto.duracao">

        <h2>Educaional</h2>
        <hr>
        <label>Interatividade</label>
        <input type="text" placeholder="Interatividade" v-model="objeto.tipodeinteratividade">
        
        <label>Recurso de Aprendizagem</label>
        <input type="text" placeholder="Recurso de Apendizagem" v-model="objeto.tipodeRecursodeAprendizagem">

        <label>nível de interatividade</label>
        <input type="text" placeholder="nível de interatividade" v-model="objeto.niveldeinteratividade">

        <label>Densidade Semântica</label>
        <input type="text" placeholder="Densidade Semântica" v-model="objeto.densidadesemantica">

        <label>Usuário Pretendido</label>
        <input type="text" placeholder="Usuário Pretendido" v-model="objeto.funcaodousuariofinalpretendido">

        <label>Contexto</label>
        <input type="text" placeholder="Contexto" v-model="objeto.contexto">

        <label>Faixa Etaria</label>
        <input type="text" placeholder="Faixa Etaria" v-model="objeto.faixaEtaria">

        <label>dificuldade</label>
        <input type="text" placeholder="dificuldade" v-model="objeto.dificuldade">

        <label>Tempo de Apredizagem</label>
        <input type="text" placeholder="Tempo de Apredizagem" v-model="objeto.TempodeAprendizagem">

        <label>idioma</label>
        <input type="text" placeholder="idioma" v-model="objeto.idioma">

        <h2>Direitos</h2>
        <hr>
        <label>custo</label>
        <input type="text" placeholder="custo" v-model="objeto.custo">

        <label>Direitos e Restrições</label>
        <input type="text" placeholder="Direitos e Restrições" v-model="objeto.DireitosautoraisRestricoes">

        <label>Descrisão</label>
        <input type="text" placeholder="Descrisão" v-model="objeto.DescrisaoDireitos">

        <h2>Relação</h2>
        <hr>
        <label>Tipo</label>
        <input type="text" placeholder="Tipo" v-model="objeto.tipoRelacao">

        <label>Recurso</label>
        <input type="text" placeholder="Recurso" v-model="objeto.recursoRelacao">

        <h2>Anotação</h2>
        <hr>
        <label>Pessoa Que fez Anotação</label>
        <input type="text" placeholder="Pessoa" v-model="objeto.pessoaAnotacao">

        <label>Data da Anotação</label>
        <input type="text" placeholder="Data da Anotação" v-model="objeto.dataanotacao">

        <label>Descrisão</label>
        <input type="text" placeholder="Descrisão" v-model="objeto.descrisaoanotacao">

        <h2>Classificação</h2>
        <hr>
        <label>Objetivo</label>
        <input type="text" placeholder="Objetivo" v-model="objeto.closificacaoObjetivo">

        <label>Taxon</label>
        <input type="text" placeholder="Taxon" v-model="objeto.taxon">

        <label>Fonte Taxon</label>
        <input type="text" placeholder="Fonte Taxon" v-model="objeto.taxonfonte">

        <label>Id Taxon</label>
        <input type="text" placeholder="Id Taxon" v-model="objeto.taxonId">

        <label>Taxon Entrada</label>
        <input type="text" placeholder="Taxon Entrada" v-model="objeto.taxonEntrada">

        <label>Descrisão da Classificação</label>
        <input type="text" placeholder="Descrisão da Classificação" v-model="objeto.classificacaoDescrisao">

        <label>Palavra Passe</label>
        <input type="text" placeholder="Palavra Passe" v-model="objeto.PalavraPasseClassificacao">

        <label>Autor</label>
        <input type="text" placeholder="Autor" v-model="objeto.autor">

        <label>Ano da Publicação</label>
        <input type="text" placeholder="Ano da Publicação" v-model="objeto.ano_pulicacao">

        <label>estado</label>
        <input type="text" placeholder="estado" v-model="objeto.estado">

        <label>N° Páginas</label>
        <input type="text" placeholder="N° Páginas" v-model="objeto.Npaginas">

        <label>editora</label>
        <input type="text" placeholder="editora" v-model="objeto.editora">
        <button class="waves-effect waves-light btn-small">Salvar</button>
      
      
      </form>
      

        <h2 class="brand-logo center"> Objetos Salvos</h2>

      <table @submit.prevent="">        
        <thead>

          <tr>
            <th>Autor</th>
            <th>Titulo</th>
            <th>N° Páginas</th>
            <th>OPÇÕES</th>
          </tr>

        </thead>

        <tbody>

          <tr v-for="objeto of objetos" :key="objeto.id">

            <td>{{ objeto.autor }}</td>
            <td>{{ objeto.titulo }}</td>
            <td>{{ objeto.Npaginas }}</td>
            <td>
              <button v-on:click="excluir()" class="waves-effect btn-small red darken-1">Excluir</button>
            </td>

          </tr>

        </tbody>
      
      </table>

    </div>

  </div>
</template>

<!-- Apartir desse ponto inicia as implemtações para a comunicação com a api -->
<script>
//inicio da definição do templete da telas
import objeto from "./servirces/Objeto" //Componente responsavel por realizar a comunicação com a api

export default{
  data(){//Variaveis
    return{
      objetos:[],//Varivel que recebe todos os objetos salvos na base de dados
      errors:[],//Gurda os erros para aletar o usuario
      objeto:{//Variavel para guardar todos os dados os Campos do IEELOM 
    titulo:'',
    catalogo:'',
    lingua:'',
    descrisao:'',
    palavrachave:'',
    corbertura:'',
    estrtura:'',
    niveldeAgregacao:0,
//Ciclo de Vida
    Versao:'',
    Status:'',
    ContribuinteFuncao:'',
    ContribuinteEntidadae:'',
    ContribuinteData:'',
//Meta-Metadados
    identificador:'',
    catalogoMeta:'',
    catalogoMetaEntrada:'',
    catalogoMetaData:'',
    EsquemaMeta:'',
    idiomameta:'',
//Tecnico
    formato:'',
    tamanho:'',
    localizacao:'',
    requisitoTipo:'',
    requisitoNome:'',
    Observacao:'',
    outrosRequitos:'',
    duracao:'',
//Educaional
    tipodeinteratividade:'',
    tipodeRecursodeAprendizagem:'',
    niveldeinteratividade:'',
    densidadesemantica:'',
    funcaodousuariofinalpretendido:'',
    contexto:'',
    faixaEtaria:'',
    dificuldade:'',
    TempodeAprendizagem:'',
    DescrisaoEducacional:'',
    idioma:'',
//Direitos
    custo:'',
    DireitosautoraisRestricoes:'',
    DescrisaoDireitos:'',
//Relacao
    tipoRelacao:'',
    recursoRelacao :'',
//Anotação
    pessoaAnotacao:'',
    dataanotacao:'',
    descrisaoanotacao:'',
//Clasificao
    closificacaoObjetivo:'',
    taxon:'',
    taxonFonte:'',
    taxonId:'',
    taxonEntrada:'',
    classificacaoDescrisao:'',
    PalavraPasseClassificacao:'',
    autor:'',
    ano_pulicacao:0,
    estado:'',
    Npaginas:0,
    editora:'' 
      },

    }
  },
//Inicio das Funções 
  mounted(){//Ao abri o site realiza a listagem dos dados é inicia a varivel que ira receber os dados para cadastro
    this.listar();
    this.objeto={}
  },
  methods:{// funções que tratam a comunicação com a api. OBS a comunicação é feita pelo componente o objeto aki é feito apenas os tratamentos dos dados

    listar(){
      objeto.listar().then(resposta => {
      this.objetos = resposta.data
    }).catch(e => {
      alert("Erro ao conectar com o backend, retonorno:"+e)
    })
    },
    salvar(){
      objeto.salvar(this.objeto).
      then(resposta =>{
        this.objeto={}
        alert(resposta.data.titulo+' salvo com Sucesso')
        this.listar()
      }).catch(e => {
        console.log(e.response.data.errors),
        alert(e.request.response)
      })
    },
      excluir(){
        alert('Em desenvolvimento')
      }      

    

  }

}

</script>

<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="//" class="brand-logo center">Produtos Front</a>
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

        <label>x1</label>
        <input type="text" placeholder="x1" v-model="objeto.x1">




      

            <button class="waves-effect waves-light btn-small">Salvar<i class="material-icons left">save</i></button>
      </form>

      <table>

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
              <button class="waves-effect btn-small blue darken-1"><i class="material-icons">create</i></button>
              <button class="waves-effect btn-small red darken-1"><i class="material-icons">delete_sweep</i></button>
            </td>

          </tr>

        </tbody>
      
      </table>

    </div>

  </div>
</template>
<script>
import objeto from "./servirces/Objeto"

export default{
  data(){
    return{
      objetos:[],
      objeto:{
    titulo:'.',
    catalogo:'.',
    lingua:'null',
    descrisao:'null',
    palavrachave:'null',
    corbertura:'null',
    estrtura:'null',
    niveldeAgregacao:0,
//Ciclo de Vida
    Versao:'.',
    Status:'.',
    ContribuinteFuncao:'.',
    ContribuinteEntidadae:'.',
    ContribuinteData:'.',
//Meta-Metadados
    identificador:'.',
    catalogoMeta:'.',
    catalogoMetaEntrada:'.',
    catalogoMetaData:'.',
    EsquemaMeta:'.',
    idiomameta:'.',
//Tecnico
    formato:'.',
    tamanho:'.',
    localizacao:'.',
    requisitoTipo:'.',
    requisitoNome:'.',
    Observacao:'.',
    outrosRequitos:'.',
    duracao:'.',
//Educaional
    tipodeinteratividade:'.',
    tipodeRecursodeAprendizagem:'.',
    niveldeinteratividade:'.',
    densidadesemantica:'.',
    funcaodousuariofinalpretendido:'.',
    contexto:'.',
    faixaEtaria:'.',
    dificuldade:'.',
    TempodeAprendizagem:'.',
    DescrisaoEducacional:'.',
    idioma:'.',
//Direitos
    custo:'.',
    DireitosautoraisRestricoes:'.',
    DescrisaoDireitos:'.',
//Relacao
    tipoRelacao:'.',
    recursoRelacao :'.',
//Anotação
    pessoaAnotacao:'.',
    dataanotacao:'.',
    descrisaoanotacao:'.',
//Clasificao
    closificacaoObjetivo:'.',
    taxon:'.',
    taxonFonte:'.',
    taxonId:'.',
    taxonEntrada:'.',
    classificacaoDescrisao:'.',
    PalavraPasseClassificacao:'.',
    autor:'.',
    ano_pulicacao:0,
    estado:'.',
    Npaginas:0,
    editora:'.', 
      },

    }
  },

  mounted(){
    objeto.listar().then(resposta => {
      console.log(resposta.data)
      this.objetos = resposta.data
    })
  },
  methods:{
    salvar(){
      objeto.salvar(this.objeto)
      // then(resposta =>{
      //   alert('Salvo com Sucesso'+resposta.log)
      // }).catch(alert('Erro as Salvar')+Error)     

    }
  }

}

</script>

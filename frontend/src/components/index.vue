<!-- inicio da definição do templete da telas -->
<template>
  <div id="app">
      <nav>
         <div class="nav-wrapper blue darken-1">
            <a  href="//" class="brand-logo center"> Seja bem-vindo ao nosso acervo de Metadados!</a>
         </div>
      </nav>
      <div >
           <v-select  multiple v-model="camposSel" :options="campos" placeholder="Todos os Campos"></v-select>
           <th><input   type="text" placeholder="Texto da busca" name="input"> </th>
           <th> <button v-on:click="Pesquisar()" class="waves-effect btn-small blue darken-1">Buscar</button> </th>
           <th> <button v-on:click="Ircad()" class="waves-effect btn-small lilac darken-1">Cadastrar</button> </th>
      </div>
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
              <button @click.prevent="Excluir(objeto.id_identificador) " class="waves-effect btn-small red darken-1">Excluir</button>
              <button @click.prevent="Alterar(objeto.id_identificador) " class="waves-effect btn-small green darken-1">Alterar</button>
            </td>

          </tr>

        </tbody>
      
      </table>

    </div>
</template>

<!-- Apartir desse ponto inicia as implemtações para a comunicação com a api -->
<script>

//inicio da definição do templete da telas
import Dados from "../servirces/Dados.js" //Componente responsavel por realizar a comunicação com a api

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
      textoPesquisa: null,
      camposSel:[],
      campos : ['titulo','catalogo','Lingua','Descrisao','palavrachave','Corbertura','Estrtura','NiveldeAgregacao','Versao','Status','ContribuinteFuncao','ContribuinteEntidadae','ContribuinteData','identificador','catalogoMeta','catalogoMetaEntrada','catalogoMetaData','EsquemaMeta','idiomameta','formato','tamanho','localizacao','requisitoTipo','requisitoNome','Observacao','outrosRequitos','duracao','tipodeinteratividade','tipodeRecursodeAprendizagem','niveldeinteratividade','densidadesemantica','funcaodousuariofinalpretendido','contexto','faixaEtaria','dificuldade','TempodeAprendizagem','DescrisaoEducacional','idioma','custo','DireitosautoraisRestricoes','DescrisaoDireitos','tipoRelacao','recursoRelacao','pessoaAnotacao','dataanotacao','descrisaoanotacao','closificacaoObjetivo','taxon','taxonFonte','taxonId','taxonEntrada','classificacaoDescrisao','PalavraPasseClassificacao','autor','ano_pulicacao','estado','Npaginas','editora'],
      textobusca : '',
      cp:''
    }
  },
//Inicio das Funções 
  mounted(){//Ao abri o site realiza a listagem dos dados é inicia a varivel que ira receber os dados para cadastro
    this.listar();
    this.objeto={}
  },
  methods:{// funções que tratam a comunicação com a api. OBS a comunicação é feita pelo componente o objeto aki é feito apenas os tratamentos dos dados

    listar(){
      Dados.listar().then(resposta => {
      this.objetos = resposta.data
    }).catch(e => {
      alert("Erro ao conectar com o backend, retonorno:"+e)
    })
    },
      Excluir(id){          
        Dados.delete(id).
        then(id=>{
        this.objeto={},
        this.listar(),
        alert('Excluido com Sucesso'),
        console.log(id);
      }).catch(e => {
        alert("Erro a excluir id:"+id+""+e),
        console.log(e.response.data.errors)
      })},  
    Pesquisar(){
        const field = document.querySelector("input[name=input]").value
        if(this.camposSel==""){            
            Dados.Buscar(field).
            then(resposta=>{
                this.objetos = resposta.data            
            }).catch(e => {
          alert("Erro ao conectar com o backend, retonorno:"+e)})
        }else{
          for(this.cp of this.camposSel){
            this.textobusca=this.textobusca+this.cp+"="+field+"&&"
          }
          Dados.BuscarCampos(this.textobusca.substring(0, this.textobusca.length - 2)).
          then(resposta=>{
            this.objetos = resposta.data 
          }).catch(e => {
          alert("Erro ao conectar com o backend, retonorno:"+e)})
        }
    },
    Ircad(){
        this.$router.push('/Cadastro')
    },
    Alterar(id){
      this.$router.push('/Cadastro/'+id)
    }
           
  }

}

</script>

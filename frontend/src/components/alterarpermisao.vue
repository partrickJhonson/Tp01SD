<template>
  <form @submit.prevent="">
    <div class="login-page">
      <div class="card">
        <div class="card-header">
          Cadastro de Usuário
        </div>
         <v-select @input="BuscarUser()" v-model="userSel"  :options="this.tlista"  placeholder="Usuários"></v-select>
        <div class="form-group">
          <input
            required
            type="Nome do Usuário"
            placeholder="Nome User"
            class="form-control"
            v-model="form.username"
          >
        </div>
        <div class="card-body">
          <div class="form-group">
            <input
              required
              type="email"
              v-model="form.email"
              class="form-control"
              placeholder="E-mail"
            >
          </div>
          <div class="form-group">
            <input
              required
              type="password"
              placeholder="Senha"
              class="form-control"
              v-model="form.password"
            >
          </div>
          <div>
          <label>Permisões do Usuário</label>  
          </div>
          <div>
          <label>
            <input  type="checkbox" :value="form.excluir"  v-model="form.excluir" />
            <span>Excluir</span>
          </label>
          <label>
            <input  type="checkbox" :value="form.alterar"  v-model="form.alterar" />
            <span>Alterar</span>
          </label>
          <label>
            <input  type="checkbox" :value="form.cadastrar"  v-model="form.cadastrar" />
            <span>Cadastar</span>
          </label>
          </div>

          <button v-on:click="Alterar()" class="btn btn-primary w-100">
            Salvar
          </button>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import Dados from "../servirces/Dados.js" //Componente responsavel por realizar a comunicação com a api
import {mapState, mapMutations} from 'vuex'
export default {
  data: () => ({
    form: {
      id:0,
      email: '',
      password: '',
      username: '',
      excluir: false,
      alterar: false,
      cadastrar: false,

    },
    userlista : {
      username:'',
      id:''
    },
    tlista:[],
    userSel:[],
    username:'',
    token:''
  }),
  computed:{
     ...mapState({
        user: state => state.usuario
      })
  },
    mounted(){//Ao abri o site realiza a listagem dos dados é inicia a varivel que ira receber os dados para cadastro
    this.listaUsers()
  },
  methods: {
      Alterar(){   
        console.log(this.form )       
        Dados.alterarUser(this.form).then(resposta=>{          
          console.log(resposta.data)
          alert('Alterado com sucesso!')
          this.$router.push('/index')
        }).catch(e => {
        try {
            alert(e.response.data['email'][0])            
        } catch (error) {
            alert(e.response.data['username'][0])
        }
      })
      },
      BuscarUser(){
        Dados.ListaUser(this.userSel).then(resposta => {
        this.form.id     = JSON.parse(resposta.request.response)['results'][0]['id']
        this.form.email     = JSON.parse(resposta.request.response)['results'][0]['email']
        this.form.password  = JSON.parse(resposta.request.response)['results'][0]['password']
        this.form.username  = JSON.parse(resposta.request.response)['results'][0]['username']
        this.form.excluir   = JSON.parse(resposta.request.response)['results'][0]['excluir']
        this.form.alterar   = JSON.parse(resposta.request.response)['results'][0]['alterar']
        this.form.cadastrar = JSON.parse(resposta.request.response)['results'][0]['cadastrar']
        console.log(this.form )
      })},
      listaUsers(){
        Dados.ListaAllUser().then(resposta => {
        this.lista = JSON.parse(resposta.request.response)['results']
        console.log(this.lista[0]['username'])
        for (let lista in this.lista ){
            this.tlista.push(this.lista[lista]['username'])
            console.log(this.tlista)
        }        
      })},

      ...mapMutations ([
           'setuser',
           'settoken'
      ]),
       

  }
}
</script>

<style >
.login-page {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
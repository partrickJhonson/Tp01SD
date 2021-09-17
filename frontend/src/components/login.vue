<template>
  <form @submit.prevent="">
    <div class="login-page">
      <div class="card">
        <div class="card-header">
          Login
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

          <th><button v-on:click="login()" class="btn btn-primary w-100">Entrar</button></th>
          <th><button v-on:click="Cadastro()" class="btn btn-primary w-100">Cadastar</button></th>

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
      email: 'patrick.jhonsom@ufvjm.edu.br',
      password: '1234567',
    },
    username:{},
    token:{}
  }),
  computed:{
     ...mapState({
        user: state => state.usuario
      })
  },
    mounted(){//Ao abri o site realiza a listagem dos dados é inicia a varivel que ira receber os dados para cadastro
    console.log(this.user)
  },
  methods: {
      login(){          
        Dados.login(this.form).then(resposta=>{         
          this.setuser      (resposta.data['username' ])
          this.settoken     (resposta.data['tokens'   ]['access'])
          this.setexcluir   (resposta.data['excluir'  ])
          this.setalterar   (resposta.data['alterar'  ])
          this.setcadastrar (resposta.data['cadastrar'])
          this.setuseradmin (resposta.data['is_superuser'])         
          this.$router.push('/index')
        }).catch(e => {
         console.log(e.response) 
         alert(e.response.data['detail'])
      })
      },
      Cadastro(){
         this.$router.push('/CadUser')
      },
      ...mapMutations ([
           'setuser',
           'settoken',
           'setexcluir',
           'setalterar',
           'setcadastrar',
           'setuseradmin'
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
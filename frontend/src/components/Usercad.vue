<template>
  <form @submit.prevent="CadastroUser()">
    <div class="login-page">
      <div class="card">
        <div class="card-header">
          Cadastro de Usuário
        </div>
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
          <button class="btn btn-primary w-100">
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
      email: 'patrick.jhonsom@ufvjm.edu.br',
      password: '1234567',
      username: '',
      excluir:   false,
      alterar:   false,
      cadastrar: false,
    },
    username:'',
    token:''
  }),
  computed:{
     ...mapState({
        user: state => state.usuario
      })
  },
    mounted(){
  },
  methods: {
      CadastroUser(){          
        Dados.CadastroUser(this.form).then(resposta=>{
          this.username=resposta.data['username']                    
          alert('Usuário Cadastrado com sucesso!')
          this.$router.push('/login')
        }).catch(e => {
        try {
            alert(e.response.data['email'][0])            
        } catch (error) {
           try {
             alert(e.response.data['username'][0])
           } catch (error) {
              alert("A senha deve ter no minimo 6 digitos")
           } 
        }
      })
      },
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
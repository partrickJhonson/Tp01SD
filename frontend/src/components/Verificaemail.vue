<template>
  <form @submit.prevent="">
    <div class="login-page">
      <div class="card">
        <div class="card-header">
          Verificar email
        </div>
        <div class="card-body">
          <div class="form-group">
            <input
              required
              type="label"
              v-model="retorno"
              class="form-control"
              placeholder=""
            >
          </div>

          <th><button v-on:click="login()" class="btn btn-primary w-100">Entrar</button></th>         
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import Dados from "../servirces/Dados.js" //Componente responsavel por realizar a comunicação com a api
export default {
  data: () => ({
      retorno:''
  }),
    mounted(){//Ao abri o site realiza a listagem dos dados é inicia a varivel que ira receber os dados para cadastro
    this.login()
  },
  methods: {
      login(){          
        Dados.verificaremail(this.$route.params.token).then(resposta=>{         
          console.log(resposta.data)
        }).catch(e => {
         alert(e.response.data['error'])
         this.retorno=e.response.data['error']
      })
      },
      Cadastro(){
         this.$router.push('/CadUser')
      }
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
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

const store = new Vuex.Store({
   state: {
       usuario:'Ninguém',
       token:'',
       excluir:false,
       alterar:false,
       cadastrar:false
   },mutations:{//funcções responsavel por alterar variaveis do state
       setuser: (state,string)=>state.usuario=string,
       settoken: (state,string)=>state.token=string,
       setexcluir: (state,boolean)=>state.excluir =boolean,
       setalterar: (state,boolean)=>state.alterar =boolean,
       setcadastrar: (state,boolean)=>state.cadastrar =boolean
   }
})

export{store}
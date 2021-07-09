<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Produtos Front</a>
      </div>
    </nav>

    <div class="container">
      <form @submit.prevent="salvar"> 
 
          <label>Titulo</label>
          <input type="text" placeholder="Titulo" v-model="objeto.titulo">

          <label>Autor</label>
          <input type="text" placeholder="Autor" v-model="objeto.autor">


          <label>ano_publicacao</label>
          <input type="number" placeholder="ano_publicacao" v-model="objeto.ano_publicacao">

          <label>estado</label>
          <input type="text" placeholder="estado" v-model="objeto.estado">

          <label>Npaginas</label>
          <input type="text" placeholder="Npaginas" v-model="objeto.Npaginas">

          <label>editora</label>
          <input type="text" placeholder="editora" v-model="objeto.editora">

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
        titulo:'',
        autor:'',
        ano_pulicacao:0,
        estado:' ',
        Npaginas:'',
        editora:''        
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
      //   alert('Salvo com Sucesso')
      // })
      

    }
  }

}

</script>

<template>
  <div id="app">
    <router-view></router-view><!--Instancia as rotas no app principal todos os componentes presentes nas rotas seram mostrados apartir desse ponto --> 
     <br>
</div>

</template>


<script>
export default{
  mounted(){ //Ao abri o site direciona pra index
     this.$router.push('/login');     
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  margin: 10px;
}
</style>
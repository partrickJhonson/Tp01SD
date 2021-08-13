<template>
  <div id="app">
    <router-view></router-view><!--Instancia as rotas no app principal -->
     <br>
</div>

</template>


<script>
export default{
  mounted(){ //Ao abri o site direciona pra index
     //this.$router.push('/index');     
  }
}
</script>

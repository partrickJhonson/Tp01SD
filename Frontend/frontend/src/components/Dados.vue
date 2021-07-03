<template>
  <div>
    <b-container>
      <b-table striped hover :items="dados"></b-table>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios'
const endpoint = 'http://localhost:8000/'
export default {
  data() {
    return {
      dados: [
        // { 'username': 'huguinho' },
        // { 'username': 'zezinho' },
        // { 'username': 'luizinho' },
      ]
    }
  },
 created() {
    axios.get(endpoint + 'cadastro/')
      .then(response => {
        this.dados = response.data.author;
      })
  }
}
</script>

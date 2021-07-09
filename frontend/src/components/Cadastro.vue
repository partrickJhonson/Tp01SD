<template>
    <form>
        <div class="form-grup">
            <label for="name">Titulo</label>
            <input type="hidden" id="titulo" titulo="id">
            <input type="text" class="form-control" id="titulo" name="titulo" placeholder="Digite o Titulo">
             </div>
             <div class="form-grup">
            <label for="name">autor</label>
            <input type="hidden" id="autor" autor="id">
            <input type="text" class="form-control" id="autor" name="autor" placeholder="Digite o autor">
             </div>
             <div class="form-grup">
            <label for="name">ano_pulicacao</label>
            <input type="hidden" id="ano_pulicacao" ano_pulicacao="id">
            <input type="text" class="form-control" id="ano_pulicacao" name="ano_pulicacao" placeholder="Digite o ano_pulicacao">
             </div>
            <div class="form-grup">
            <label for="name">estado</label>
            <input type="hidden" id="estado" estado="id">
            <input type="text" class="form-control" id="estado" name="estado" placeholder="Digite o estado">
             </div>
            <div class="form-grup">
            <label for="name">Npaginas</label>
            <input type="hidden" id="Npaginas" Npaginas="id">
            <input type="text" class="form-control" id="Npaginas" name="Npaginas" placeholder="Digite o Npaginas">
             </div> 
            <div class="form-grup">
            <label for="name">editora</label>
            <input type="hidden" id="editora" editora="id">
            <input type="text" class="form-control" id="editora" name="editora" placeholder="Digite o editora">
             </div> 
        <button v-on:click="onSubmit" type="button" class="btn btn-primary">Enviar</button>    
    </form>    
</template>
<script>
  export default {
    data() {
      return {
        form: {
          titulo: this.titulo,
          name: this.name,
          food: this.form.titulo,
          checked: []
        },
        foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },

    }
  }
</script>
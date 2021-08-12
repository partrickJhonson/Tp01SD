import { http } from "./config"; // importa a  constante que contem o endereço da api

export default {
    listar: () => {
        return http.get('cadastro/?ordering=-EntradaNoCatalogo')
    },

    salvar: (objeto) => {
        return http.post('cadastro/', objeto)
    },
    Buscar: (textoBusca) => {
        return http.get('buscar/?search='+textoBusca)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },
    BuscarId: (textoBusca) => {
        return http.get('buscar/?id_identificador='+textoBusca)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },   
    delete: (id) => {
        return http.delete('buscar/'+id)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },
    alterar:(id,objeto)=>{
        return http.put('cadastro/'+objeto.id_identificador+'/', objeto)
    }
}
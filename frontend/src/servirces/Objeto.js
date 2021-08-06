import { http } from "./config"; // importa a  constante que contem o endereço da api

export default {
    listar: () => {
        return http.get('cadastro')
    },

    salvar: (objeto) => {
        return http.post('cadastro/', objeto)
    },
    Buscar: (textoBusca) => {
        return http.get('buscar/?autor='+textoBusca)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },
    BuscarId: (textoBusca) => {
        return http.get('buscar/?id_bidentificador='+textoBusca)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },   
    delete: (id) => {
        return http.delete('buscar/'+id)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },
}
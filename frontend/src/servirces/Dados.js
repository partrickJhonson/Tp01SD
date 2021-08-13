import { http } from "./config"; // importa a  constante que contem o endereço da api

export default {
    listar: () => {
        return http.get('cadastro/?ordering=-EntradaNoCatalogo')
    },

    salvar: (objeto) => {
        return http.post('cadastro/', objeto)
    },
    Buscar: (textoBusca) => {
        return http.get('buscar/?search='+textoBusca)//BUsca em todos os campos
    },
    BuscarCampos: (textoBusca) => {
        return http.get('buscar/?'+textoBusca)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },
    BuscarId: (textoBusca) => {
        return http.get('buscar/?id_identificador='+textoBusca)//Busca para alterar
    },   
    delete: (id) => {
        return http.delete('cadastro/'+id)//
    },
    alterar:(id,objeto)=>{
        return http.put('cadastro/'+objeto.id_identificador+'/', objeto)
    }
}
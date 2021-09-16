import { http } from "./config"; // importa a  constante que contem o endereço da api

export default {
    listar: () => {
        return http.get('api/v1/cadastro/?ordering=-EntradaNoCatalogo')
    },

    salvar: (objeto) => {
        return http.post('api/v1/cadastro/', objeto)
    },
    Buscar: (textoBusca) => {
        return http.get('api/v1/buscar/?search='+textoBusca)//BUsca em todos os campos
    },
    BuscarCampos: (textoBusca) => {
        return http.get('api/v1/buscar/?'+textoBusca)//Montar uma string com campo concatenando todos os campos com a texto a ser buscado
    },
    BuscarId: (textoBusca) => {
        return http.get('api/v1/buscar/?id_identificador='+textoBusca)//Busca para alterar
    },   
    delete: (id) => {
        return http.delete('api/v1/cadastro/'+id)//
    },
    alterar:(id,objeto)=>{
        return http.put('api/v1/cadastro/'+objeto.id_identificador+'/', objeto)
    },
    login:(dados)=>{
        return http.post('auth/Login/', dados)
    },
    CadastroUser:(dados)=>{
        return http.post('auth/register/', dados)
    },
    ListaAllUser:()=>{
        return http.get('api/v1/buscaruser/')
    },
    ListaUser:(name)=>{
        return http.get('api/v1/buscaruser/?username='+name)
    },
    alterarUser:(form)=>{
        return http.put('api/v1/buscaruser/'+form.id+'/',form)
    },
    verificaremail:(token)=>{
        return http.get('auth/emailverify/?token='+token)
    }
}
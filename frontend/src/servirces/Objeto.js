import { http } from "./config"; // importa a  constante que contem o endereço da api

export default {
    listar: () => {
        return http.get('cadastro')
    },

    salvar: (objeto) => {
        return http.post('cadastro/', objeto)
    }
}
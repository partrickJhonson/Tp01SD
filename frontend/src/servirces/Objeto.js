import { http } from "./config";

export default {
    listar: () => {
        return http.get('cadastro')
    },

    salvar: (objeto) => {
        return http.post('cadastro/', objeto)
    }
}
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Cadastro from './components/Cadastro'
import Index    from './components/index'
import login    from './components/login'
import { store } from './servirces/vuex'
import Usercad    from './components/Usercad'
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'
import './assets/scss/app.scss'
import alterarpermisao from './components/alterarpermisao'

Vue.use(VueRouter)
Vue.component("v-select",vSelect);
const router = new VueRouter({
    mode: "history",
    routes: [
        {path: "/",redirect: Index},//Direciona o user para a rota inicia
        {path: '/Cadastro/:id',component: Cadastro},//Altera
        {path: '/Cadastro',component: Cadastro},//CriarNovo
        {path: "/index",component: Index},
        {path: "/login",component: login},
        {path: "/CadUser",component: Usercad},
        {path: "/alterarpermisao",component: alterarpermisao},
        {path: "",redirect: Index},
    ]

})

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app')
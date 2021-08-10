import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Cadastro from './components/Cadastro'
import Index    from './components/index'

Vue.use(VueRouter)
const router = new VueRouter({
    mode: "history",
    routes: [
        {path: "/",redirect: Index},//Direciona o user para a rota inicia
        {path: '/Cadastro/:id',component: Cadastro},
        {path: "/index",component: Index},
        {path: "",redirect: Index},
    ]

})

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Cadastro from './components/Cadastro'
import Index    from './components/index'

Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        {path: '/Cadastro',component: Cadastro},
        {path: '/index'   ,component: Index},
        {path: '/'         ,redirect : Cadastro},//Direciona o user para a rota inicia
    ]

})

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
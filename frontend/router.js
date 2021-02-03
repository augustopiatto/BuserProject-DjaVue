import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Famosos from '~/pages/famosos.vue'
import Cidades from '~/pages/cidades.vue'
import Mypage from '~/pages/mypage.vue'
import NomedoFamoso from '~/pages/user/_username/findex.vue'
import NomedaCidade from '~/pages/user/_city/cindex.vue'
import Sobre from '~/pages/sobre.vue'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/famosos', component: Famosos, name: 'famosos'},
    {path: '/cidades', component: Cidades, name: 'cidades'},
    { path: '/mypage', component: Mypage, name: 'mypage' },
    {path: '/famosos/:nomedofamoso?', component: NomedoFamoso, name: 'nomedofamoso'},
    {path: '/cidades/:nomedacidade?', component: NomedaCidade, name: 'nomedacidade'},
    {path: '/sobre', component: Sobre, name: 'sobre'}
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}

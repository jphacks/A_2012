import { createRouter, createWebHistory } from 'vue-router'
const routes = [
  {
    path: '/',
    name: 'Top',
    component: () => import(/* webpackChunkName: "top" */ '../views/Top.vue')
  },
  {
    path: '/set',
    name: 'Set',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "set" */ '../views/Set.vue')
  },
  {
    path: '/start',
    name: 'Start',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "start" */ '../views/Start.vue')
  },
  {
    path: '/join',
    name: 'Join',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../components/NMButton.vue')
  },
  {
    path: '/history',
    name: 'History',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../components/NMButton.vue')
  },
  {
    path: '/talk',
    name: 'Talk',
    component: () => import(/* webpackChunkName: "about" */ '../views/Talk.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

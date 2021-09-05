import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TopTenUSCovidCases from '../views/TopTenUSCovidCases.vue'
import TopTenUSCovidDeaths from '../views/TopTenUSCovidDeaths.vue'
import TopTenUSCovidTests from '../views/TopTenUSCovidTests.vue'
import TotalUSCovidCases from '../views/TotalUSCovidCases.vue'
import TotalUSCovidDeaths from '../views/TotalUSCovidDeaths.vue'
import TotalUSCovidTests from '../views/TotalUSCovidTests.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/topTenUSCovidCases',
    name: 'TopTenUSCovidCases ',
    component: TopTenUSCovidCases 
  },
  {
    path: '/totalUSCovidCases',
    name: ' TotalUSCovidCases',
    component: TotalUSCovidCases
  },
  {
    path: '/topTenUSCovidDeaths',
    name: 'TopTenUSCovidDeaths',
    component: TopTenUSCovidDeaths
  },
  {
    path: '/totalUSCovidDeaths',
    name: 'TotalUSCovidDeaths',
    component: TotalUSCovidDeaths
  },
  {
    path: '/topTenUSCovidTests',
    name: 'TopTenUSCovidTests',
    component: TopTenUSCovidTests
  },
  {
    path: '/totalUSCovidTests',
    name: 'TotalUSCovidTests',
    component: TotalUSCovidTests
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

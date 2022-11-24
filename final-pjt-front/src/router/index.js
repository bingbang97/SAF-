import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView'

import MovieDetailView from '@/views/MovieDetailView'

import CommunityView from '@/views/CommunityView'
import ACreateView from '@/views/ACreateView'
import ADetailView from '@/views/ADetailView'
import AUpdateView from '@/views/AUpdateView'

import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import ProfileView from '@/views/ProfileView'
import PasswordChangeView from '@/views/PasswordChangeView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },

  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },

  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'ACreateView',
    component: ACreateView
  },

  {
    path: '/community/update/:id',
    name: 'AUpdateView',
    component: AUpdateView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/passwordchange',
    name: 'PasswordChangeView',
    component: PasswordChangeView
  },

  {
    path: '/profile/:id',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/:id',
    name: 'ADetailView',
    component: ADetailView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

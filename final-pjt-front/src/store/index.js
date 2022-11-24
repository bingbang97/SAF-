import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'


const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)



export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    articles: [],
    comments: [],

    topmovies: [],
    timemovies: [],
    nowplayingmovies: [],
    urcmovies: [],
    ssafyplusmovies: [],

    user : null,
    token: null,

    authError: null,
    isAuthError: false,

  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    },

    isAuthError: state => state.isAuthError,
    authError: state => state.authError,

  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
    },
    GET_COMMENTS(state, comments){
      state.comments = comments
    },

    GET_TOP_MOVIES(state, movies){
      state.topmovies = movies
    },

    GET_TIME_MOVIES(state, movies){
      state.timemovies = movies
    },
    GET_NOW_PLAYING_MOVIES(state, movies){
      state.nowplayingmovies = movies
    },
    GET_RECOMMEND_MOVIE(state, movies){
      state.urcmovies = movies
    },
    GET_SAFPLUS_MOVIE(state, movies){
      state.ssafyplusmovies = movies
    },
    SIGN_UP(state, token){
      state.token = token
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers:{
          Authorization: `Token ${state.token}`
        },
      })
      .then((response) => {
        state.user = response.data
        state.authError = null,
        state.isAuthError = false,
        router.push({ name: 'HomeView' })
      })
      .catch((error)=> {
        console.log(error)
      })
    },
    SAVE_TOKEN(state, token){
      state.token = token
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers:{
          Authorization: `Token ${state.token}`
        },
      })
      .then((response) => {
        state.user = response.data
        state.authError = null,
        state.isAuthError = false,
        router.push({ name: 'HomeView' })
      })
      .catch((error)=> {
        console.log(error)
      })
    },
    LOG_OUT(state){
      state.token = !state.token
      state.user = null
      router.push({ name: 'HomeView' })
    },

    SET_AUTH_ERROR: (state, error) => {
      state.authError = error
      state.isAuthError = true
    },

  },
  actions: {
    getArticles(context){
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/community/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        },
      })
      .then((response) => {
        context.commit('GET_ARTICLES', response.data)
    })
      .catch((error) => {
        console.log(error)
      })
    },
    getComments(context){
      axios({
        method: 'get',
        url : `${API_URL}/api/v1/comments/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        },
      })
      .then((response) => {
        context.commit('GET_COMMENTS', response.data)
    })
      .catch((error) => {
        console.log(error)
      })
    },
    getTopMovies(context){
      axios({
        method : 'get',
        url : `${API_URL}/movies/top20/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        },
      })
      .then((response) => {
        context.commit('GET_TOP_MOVIES', response.data)
    })
      .catch((error) => {
        console.log(error)
      })
    },
    getTimeMovies(context){
      axios({
        method : 'get',
        url : `${API_URL}/movies/timerelated/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        },
      })
      .then((response) => {
        context.commit('GET_TIME_MOVIES', response.data)
    })
      .catch((error) => {
        console.log(error)
      })
    },
    getNowPlayingMovies(context){
      axios({
        method : 'get',
        url : `${API_URL}/movies/nowplaying/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        },
      })
      .then((response) => {
        context.commit('GET_NOW_PLAYING_MOVIES', response.data)
    })
      .catch((error) => {
        console.log(error)
      })
    },
    getRecommendMovie(context, payload){
      axios({
        method: 'post',
        url: `${API_URL}/movies/userrecommend/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        },
        data:{
          like_genre1 : payload.like_genre1,
          like_genre2 : payload.like_genre2,
          like_genre3 : payload.like_genre3,
        }
      })
      .then((res)=>{
        context.commit('GET_RECOMMEND_MOVIE', res.data)
      })
      .catch((err) =>{
        console.log(err)
      })
    },
    getSsafyPlusMovie(context){
      axios({
        method: 'get',
        url: `${API_URL}/movies/ssafyplus/`,
      })
      .then((res)=>{
        context.commit('GET_SAFPLUS_MOVIE', res.data)
      })
      .catch((err) =>{
        console.log(err)
      })
    },
    signUp(context, payload){
      axios({
        method: 'post',
        url:`${API_URL}/accounts/signup/`,
        data:{
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
          like_genre1: payload.like_genre1,
          like_genre2: payload.like_genre2,
          like_genre3: payload.like_genre3,
        }
      })
      .then((response)=>{
        context.commit('SIGN_UP', response.data.key)
      })
      .catch((error)=>{
        console.log(error)
        context.commit('SET_AUTH_ERROR', error.response.data)
      })
    },
    logIn(context, payload){
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data:{
          username,
          password,
        }
      })
      .then((response)=>{
        context.commit('SAVE_TOKEN', response.data.key)
      })
      .catch((error)=>{
        console.log(error)
        context.commit('SET_AUTH_ERROR', error.response.data)
      })
    },
    logOut(context){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`
      })
      .then(()=>{
        context.commit('LOG_OUT')
      })
      .catch((error)=>{
        console.log(error)
      })
    },
  },
  modules: {
  }
})

<template>
  <div class="bc">
    <div class="profile-page">
      <div class="page-header header-filter" data-parallax="true"></div>
      <div class="main main-raised">
      <div class="profile-content">
        <div class="container">
          <div class="row">
            <div class="profile">
              <div class="avatar">
                <img src="https://xsgames.co/randomusers/avatar.php?g=male" alt="Circle Image" id="profile-img" class="img-raised rounded-circle img-fluid">
              </div>
              <div class="name">
                <h3 class="title">{{ user?.username }}</h3>
                <button class="btn btn-light">
                  <router-link 
                    v-if="user?.id === this.$store.state.user.pk"
                    :to="{name : 'PasswordChangeView'}"
                  >change password</router-link>
                </button>

              </div>
          <div class="row">
              <div class="profile-tabs">
                <div id="favorite">
                  <div>Favorite Genre</div>
                  <br>
                  <div class="badge-wrap">
                    <span class="badge rounded-pill ">{{ user?.like_genre1 }}</span>
                    <span class="badge rounded-pill ">{{ user?.like_genre2 }}</span>
                    <span class="badge rounded-pill ">{{ user?.like_genre3 }}</span>
                  </div>
                </div>
                <div id="article">
                  <div>WRITTEN ARTICLE</div>
                  <br>
                  <span
                    class="badge rounded-pill"
                    v-for="article in articles"
                    :key="article?.id"
                  >
                    <i class="bi bi-justify"></i>
                    <router-link :to="{ name : 'ADetailView', params: {id : `${article?.id}`} }">{{article?.title}}</router-link>
                  </span>
                </div>

                <div id="article">
                  <div>LIKED ARTICLE</div>
                  <br>
                  <span
                    class="badge rounded-pill"
                    v-for="article in likeArticles"
                    :key="article?.id"
                  >
                    <i class="bi bi-heart-fill"></i> 
                    <router-link :to="{ name : 'ADetailView', params: {id : `${article?.id}`} }">{{article?.title}}</router-link>
                  </span>
                </div>                

                <div id="movie">
                  <div>RATED MOVIE</div>
                  <br>
                  <ProfileMovieList
                    :recommendMovies="recommendMovies"
                  />
                  
                </div>
            </div>
          </div>
            <button id="quit"
              v-if="user?.id === this.$store.state.user.pk"
              @click="deleteUser"
              class="btn btn-light"
              >회원탈퇴
            </button>
          </div>
        </div>
      </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileMovieList from '@/components/ProfileMovieList.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data(){
    return{
      user : null,
      articles : [],
      likeArticles: [],
      recommendMovies : [],
    }
  },
  components:{
    ProfileMovieList
  },
  computed: {
    pageId(){
      return this.$route.params.id
    },
  },
  methods:{
    getUsers(){
      axios({
        method: 'get',
        url : `${API_URL}/customaccounts/userinfo/${this.$route.params.id}/`,
      })
      .then((response) => {
        // console.log(response)
        this.user = response.data
      })
      .catch((error) =>{
        console.log(error)
      })
    },
    deleteUser(){
      axios({
        method: 'delete',
        url : `${API_URL}/customaccounts/signount/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then(() => {
        // console.log(res)
        this.$store.commit('LOG_OUT')
        this.$router.push({ name : 'HomeView' }).catch(()=>{});
      })
      .catch((error) =>{
        console.log(error)

      })
    },
    getArticles(){
      this.$store.state.articles.forEach(article => {
        if (String(article.user) === this.pageId){
          // console.log(article)
          this.articles.push(article)
        }
      })
    },
    getLikeArticle(){
      this.$store.state.articles.forEach((article) => {
        // console.log(article)
        if (article.like_users.includes(Number(this.pageId))){
          // console.log(article)
          this.likeArticles.push(article)
        }
      })
        // console.log(this.likeArticles)
    },

    getRecommendMovies(){
      axios({
        method: 'get',
        url : `${API_URL}/movies/comments/`,
      })
      .then((res) => {
        // console.log(res)
        res.data.forEach((comment)=>{
          if(String(comment.user) === this.pageId){
            this.recommendMovies.push(comment)
          }
        })
        // console.log(this.recommendMovies)
      })
      .catch((error) =>{
        console.log(error)

      })
    },
  },
  
  created(){
    this.getUsers()
    this.getArticles()
    this.getRecommendMovies()
    // this.getProfile()
    this.getLikeArticle()
  }
  

}
</script>

<style scoped>
  .bc {
    -webkit-font-smoothing: antialiased;
    overflow-y: scroll;
    scrollbar-width: none;
    min-width: 300px;
  }

  .bc::-webkit-scrollbar{
    display:none;
  }

  #favorite {
    /* font-size: .75rem !important; */
    font-weight: 500;
    margin-bottom: 30px;
    line-height: 1.5em;
    text-transform: uppercase;
  }

  .profile-page .page-header {
    height: 280px;
    background-position:center;
  }

  .page-header {
    height: 100vh;
    background-size: cover;
    margin: 0;
    padding: 0;
    border: 0;
    display: flex;
    align-items: center;
    scrollbar-width: none;
  }

  .main-raised {
    margin: -60px 30px;
    border-radius: 6px;
    box-shadow: 0 16px 24px 2px rgba(0,0,0,.14), 0 6px 30px 5px rgba(0,0,0,.12), 0 8px 10px -5px rgba(0,0,0,.2);
    
  }

  .main {
    background: #FFF;
    position: relative;
  
    z-index: 3;
  }

  .profile-page .profile {
    text-align: center;
  }

  .avatar {
    /* background-color: beige; */
    height: 80px;
  }

  .name {
    margin-bottom: 50px;
  }

  #profile-img {
    max-width: 160px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-50%,0);
    -moz-transform: translate3d(0,-50%,0);
    -o-transform: translate3d(0,-50%,0);
    -ms-transform: translate3d(0,-50%,0);
    transform: translate3d(0,-50%,0);
  }

  .img-raised {
    box-shadow: 0 5px 15px -8px rgba(0,0,0,.24), 0 8px 10px -5px rgba(0,0,0,.2);
    z-index: 100;

  }

  .rounded-circle {
    border-radius: 50%!important;
  }  

  .img-fluid {
    max-width: 100%;
    height: auto;
  }

  .title {
    margin-top: 30px;
    margin-bottom: 25px;
    min-height: 32px;
    color: #3C4858;
    font-weight: 700;
  }

  .btn {
    position: relative;
    padding: 3px 15px;
    margin: .3125rem 1px;
    font-size: .75rem;
    font-weight: 400;
    line-height: 1.428571;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0;
    border: 0;
    border-radius: .2rem;
    outline: 0;
    transition: box-shadow .2s cubic-bezier(.4,0,1,1), background-color .2s cubic-bezier(.4,0,.2,1);
    will-change: box-shadow,transform;
  }
  .btn:hover a{
    text-decoration: none;
    color: rgb(255, 255, 255);
  }

  a {
    text-decoration: none;
    color: black;
  }

  .badge:hover a{
    text-decoration: none;
    color: #ffffff;
  }

  span {
    margin : 5px;
    background-color: aquamarine;
  }

  #article {
    margin-top: 50px;
    margin-bottom: 50px;
  }

  #movie {
    margin-top: 50px;
    margin-bottom: 50px;
  }

  #quit {
    margin: 30px;
    float: right;
    color: white;
  }

  .badge-wrap {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .badge {
    /* width: 140px; */
    /* height: 45px; */
    font-family: 'Roboto', sans-serif;
    font-size: 11px;
    /* text-transform: uppercase; */
    letter-spacing: 2.5px;
    font-weight: 500;
    color: #000;
    background-color: #fff;
    border: none;
    border-radius: 45px;
    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease 0s;
    cursor: pointer;
    outline: none;
    }

  .badge:hover {
    background-color: #13034e;
    box-shadow: 0px 15px 20px rgba(9, 1, 43, 0.4);
    color: #fff;
    transform: translateY(-7px);
  }
</style>
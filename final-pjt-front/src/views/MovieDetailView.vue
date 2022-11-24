<template>
  <div id="md" :style="{'background-image':  this.movieUrl}">
    <div id="mvd">
      <div id="container">

        <div class="logo">
          <div v-if="movieLogo">
            <img 
            :src="`https://image.tmdb.org/t/p/w400/${movie?.logo_path}`" 
            alt=""
            >
          </div>
          <div v-else >
            <div id="hidden-title">{{ movie?.title }}</div>
          </div>
        </div>


        <div class="badge-wrap">
          <span
            v-for="(genre, idx) in movie?.genres"
            :key="idx"
            class="badge rounded-pill "
          >{{ movieGenresList[genre] }}
          </span>
        </div>
        <br>

        <div class="released-date">
          <div>{{ movie?.released_date }}</div>
        </div>
        <br>

        <div class="overview">

          <p>{{ movie?.overview }}</p>

        </div>
        <br>
        
        <button type="button" class="btn btn-dark" @click="showYoutbeLink">예고편 보기</button>

        <div id="overlay" :class="{'show': showYoutube }">
            <iframe
              width="800px"
              height="450px"
              :src="`https://www.youtube.com/embed/${movie?.youtube_id}`"
            >
            </iframe>
            <button type="button" class="btn-close btn-close-white" aria-label="Close" @click="closeButton"></button>
        </div>

        <br>
        <br>
        <hr class="hr3px">
        <br>
        <MCommentCreateForm
          @commentSignal="commentSignal"
        />
        <br>
        <!-- <hr> -->
        <br>
        <MCommentList
          :comments="comments"    
        />
      </div>
    </div>
  </div>
</template>

<script>
import MCommentCreateForm from '@/components/MCommentCreateForm'
import MCommentList from '@/components/MCommentList'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    MCommentCreateForm,
    MCommentList
  },
  data(){
    return {
      movie: null,
      movieLogo: null,
      comments: null,
      movieUrl : null,
      rate: null,
      movieGenresList:{
        28: "Action",
        12: "Adventure",
        16: "Animation",
        35: "Comedy",
        80: "Crime",
        99: "Documentary",
        18: "Drama",
        10751: "Family",
        14: "Fantasy",
        36: "History",
        27: "Horror",
        10402: "Music",
        9648: "Mystery",
        10749: "Romance",
        878: "Science Fiction",
        10770: "TV Movie",
        53: "Thriller",
        10752: "War",
        37: "Western",
      },
      showYoutube: false,
    }
  },
  created() {
    this.getMovieDetail()
  }, 
  methods :{
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/movie/${this.$route.params.id}/`,
      })
      .then((response)=> {
        this.movie = response.data
        this.comments = response.data.moviecomment_set
        if (response.data.logo_path === 'does_not_exists'){
          this.movieLogo = false
        }
        else{
          this.movieLogo = response.data.logo_path
        }
        response.data.moviecomment_set.forEach(element => {
          this.rate += (element.vote_rate / (response.data.moviecomment_count ) )
        });
        this.movieUrl = `url(https://image.tmdb.org/t/p/w1280/${response.data.related_picture_path})`
      })
      .catch((error) => {
        console.log(error)
        console.log(this.$route.params.id)
      })
    },
    commentSignal() {
      this.getMovieDetail()
    },
    closeButton(){
      this.showYoutube = false
    },
    showYoutbeLink(){
      this.showYoutube = true
    }
  },
}
</script>

<style scoped>

  *{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family: 'Nanum Gothic', sans-serif;
    color: white;
  }
  #md{
    display: grid;
    background-position: center;
    background-size: cover;
    width: 100%;
    overflow: auto;
    height: 100vh;
    overflow-y: scroll;
    scrollbar-width: none;
  }
  #md::-webkit-scrollbar{
    display: none;

  }
  #mvd{
    width: 100%;
    background: linear-gradient(to bottom, rgba(0, 0, 0, 0.3), rgba(3, 2, 10, 1));
    background-attachment: fixed;
  }
  #container{
    margin: 20px;
    margin-left: 50px;
    margin-right: 50px;
  }
  .logo div img{
    /* margin-left: 30px; */
    margin-top: 30px;
    margin-bottom: 50px;
  }
  .logo div h1{
    margin-top: 220px;
    margin-left: 30px;
    margin-bottom: 55px;
  }
  .overview{
    width: 70vw;
    max-width: 600px;
  }
  .badge-wrap {
    height: 100%;
    display: flex;
    align-items: center;
    /* justify-content: center; */
  }

  .badge {
    /* width: 140px; */
    /* height: 45px; */
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    text-transform: uppercase;
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
    margin: 5px;
    margin-bottom: 13px;
    }

  /* .badge:hover {
    background-color: #13034e;
    box-shadow: 0px 15px 20px rgba(9, 1, 43, 0.4);
    color: #fff;
    transform: translateY(-7px);
  } */
  .released-date{
    font-size: 13px;
  }
  /* 오버레이 설정 */
  #overlay{
    position: fixed;
    top:0; left:0;
    width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.8);
    z-index: 999;
    /* 시작시 보이지 않게 처리 */
    visibility: hidden;
    opacity: 0;
    transition: all 0.5s;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  /* 오버레이를 보여 줄때 사용 */
  #overlay.show {
    visibility: visible;
    opacity: 1;
  }
  #overlay button{
    position: absolute;
    top: 120px;
    right : 100px;
  }
  .hr3px{
    border: 0;
    height: 3px;
    background: #ccc;
  }


  @import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');  
  #hidden-title{
    font-size: 50px;
    margin-top: 110px;
    margin-bottom: 110px;
    font-family: 'Do Hyeon', sans-serif;
  }


  .input-box {
    width: 50px;
    margin: 7px;
    border-radius: 5px;
  }
  .textbox {
    position: relative;
    display: flex;
    justify-content: left;
  }

  .textbox input[type="text"] {
    width: 90%; 
    height: 35px;  
    line-height : normal;  
    padding: .8em .5em; 
    font-family: inherit;
    border: 1px solid #999;
    border: none; 
    outline-style: none; 
    -webkit-appearance: none;  
    -moz-appearance: none;
    appearance: none;
    background-color: transparent;
  }

  .textbox input[type="text"]:hover {
    box-shadow: inset 4px 4px 60px 8px rgba(175, 175, 175, 0.2);
  }
  
  input::placeholder {
    font-size: 13px;
  }
  
</style>
<template>
  <div>
    <div id="title">{{ user.username }}님을 위한 추천 영화</div>
    <MovieList
      :movies="movies"
    />
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import MovieList from '@/components/MovieList'
export default {
  name: 'UserRecommendMovie',
  components:{
    MovieList,
  },
  computed:{
    movies(){
      return this.$store.state.urcmovies
    },
    user() {
      return this.$store.state.user
    }
  },
  methods:{
    getCustomMovie(){
      axios({
        method: 'get',
        url : `${API_URL}/customaccounts/userinfo/${this.$store.state.user.pk}/`,
      })
      .then((response) => {
        // console.log(response)
        const like_genre1 = response.data.like_genre1
        const like_genre2 = response.data.like_genre2
        const like_genre3 = response.data.like_genre3
        const payload = {
          like_genre1,
          like_genre2,
          like_genre3,
        }
        this.$store.dispatch('getRecommendMovie', payload)
        // console.log(payload)
      })
      .catch((error) =>{
        console.log(error)
      })
    },
  },
  mounted(){
    this.getCustomMovie()
  }
}
</script>

<style scoped>
  #title {
    margin-top: 20px;
    padding:2px;
    margin-left: 15px;
    color: white;
    font-size: 20px;
    font-weight: bold;
  }
</style>
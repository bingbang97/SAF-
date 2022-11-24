<template>
  <div>
    <div id="title">지금 이시간 </div>
    <MovieList
      :movies="movies"
    />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
export default {
  name : 'TimeRelatedMovie',
  components:{
    MovieList,
  },
  computed:{
    movies(){
      return this.$store.state.timemovies
    },
  },
  methods:{
    getTimeMovies(){
      this.$store.dispatch('getTimeMovies')
    }
  },
  created(){
    this.getTimeMovies()
  }

}
</script>

<style scoped>
  #title {
    padding:2px;
    margin-left: 15px;
    color: white;
    font-size: 20px;
    font-weight: bold;
  }  
</style>
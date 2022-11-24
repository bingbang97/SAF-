<template>
  <div>
    <div id="title">Top 20</div>
    <MovieList
      :movies="movies"
    />
  </div>
</template>


<script>


import MovieList from '@/components/MovieList'
export default {
  name : 'TopMovie',
  components:{
    MovieList,
  },
  computed:{
    movies(){
      return this.$store.state.topmovies
    },
  },
  methods:{
    getTopMovies(){
      this.$store.dispatch('getTopMovies')
    }
  },
  created(){
    this.getTopMovies()
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
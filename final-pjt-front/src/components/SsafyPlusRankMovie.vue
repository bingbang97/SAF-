<template>
  <div>
    <div id="title">SSAFY +</div>
    <div v-if="isplusmovie">
      <MovieList
      :movies="topmovies"
    />
    </div>
    <div v-else>
      <MovieList
      :movies="movies"
    />
    </div>
    
  </div>
</template>


<script>


import MovieList from '@/components/MovieList'
export default {
  name : 'SsafyPlusRankMovie',
  data(){
    return{
      isplusmovie : false,
    }
  },
  components:{
    MovieList,
  },
  computed:{
    movies(){
      return this.$store.state.ssafyplusmovies
    },
    topmovies(){
      return this.$store.state.topmovies
    }
    
  },
  methods:{
    getSsafyPlusMovie(){
      this.$store.dispatch('getSsafyPlusMovie')
      if(this.$store.state.ssafyplusmovies.length === 0){
        // console.log(this.$store.state.ssafyplusmovies)
        this.isplusmovie = true
      }
    },
    getTopMovies(){
      this.$store.dispatch('getTopMovies')
    }
  },
  created(){
    this.getSsafyPlusMovie()
    this.getTopMovies()
    // console.log(this.isplusmovie)
  }

}
</script>

<style scoped>
  #title {
    padding:2px;
    margin-left: 15px;
    color: white;
    font-size: 20px;
  }
</style>
<template>

  <swiper-slide>
    <div @click="toMovieDetail" class="poster_picture">
      <img 
        :src="`https://image.tmdb.org/t/p/w200/${movie?.poster_path}`" 
        alt="그림"
      >
      <span class="poster_text"

      >{{ movie?.title }}</span>
    </div>
  </swiper-slide>

</template>

<script>
import {SwiperSlide} from 'vue-awesome-swiper'

export default {
  name: 'MovieListItem',
  components:{
    SwiperSlide
  },
  props:{
    movie:Object,
  },
  methods: {
    toMovieDetail(){
      this.$router.push({ name : 'MovieDetailView', params: { id : this.movie.id } })
    },
  }
}
</script>

<style>
  .poster_picture{
    display: flex;
    justify-content: center;
    align-items: center;
    place-items: center;
    margin: 10px;
  }
  .poster_picture img{
    max-width: 100%;
    width: 100%;
    vertical-align: middle;
    border-radius: 10px;
    transition: all 0.2s linear;
    
  }
  .poster_text{
    width: 100%;
    /* background-color: #44444460; */
    color: #ffffff;
    position: absolute;
    text-align: center;
    opacity: 0;
    z-index: 50;
    font-size: 1em;
    
    
  }
  .poster_picture:hover .poster_text{
    opacity: 1;
  }
  .poster_picture:hover img{
    transform: scale(1.1);
    filter: brightness(50%);
    overflow: auto;
    margin: auto;
  }

</style>
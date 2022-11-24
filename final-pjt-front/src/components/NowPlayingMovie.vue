<template>
  <div id="nowplay">
    <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="3" aria-label="Slide 4"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <iframe 
            :src="`https://www.youtube.com/embed/${movies[0].youtube_id}?autoplay=1&mute=1`"
            class="d-block w-100"
            width="100vw"
            height="300vh"
          >
          </iframe>
        </div>
        <div class="carousel-item">
          <iframe 
            :src="`https://www.youtube.com/embed/${movies[1].youtube_id}?autoplay=1&mute=1`"
            class="d-block w-100"
            width="100vw"
            height="300vh"
          >
          </iframe>
        </div>
        <div class="carousel-item">
          <iframe 
            :src="`https://www.youtube.com/embed/${movies[2].youtube_id}?autoplay=1&mute=1`"
            class="d-block w-100"
            width="100vw"
            height="300vh"
          >
          </iframe>
        </div>
        <div class="carousel-item">
          <iframe 
            :src="`https://www.youtube.com/embed/${movies[3].youtube_id}?autoplay=1&mute=1`"
            class="d-block w-100"
            width="100vw"
            height="300vh"
          >
          </iframe>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>


export default {
  name : 'NowPlayingMovie',
  computed:{
    movies(){
      // console.log(this.$store.state.nowplayingmovies);
      return this.$store.state.nowplayingmovies
    },
  },
  methods:{
    getTimeMovies(){
      this.$store.dispatch('getNowPlayingMovies')
    },
  },
  created(){
    this.getTimeMovies()
  }

}
</script>

<style>
#nowplay{
  margin: 10px;
}
#area {
  position: relative; /* absolute는 부모가 relative일 때 부모를 따라간다. */
  width: 70%;
  padding-bottom: 39.375%; /* 16:9 비율 */
}

#video {
  position: absolute;
  width: 100%; /* 부모에 맞게 꽉 채운다. */
  height: 100%;
}
.iframeContainer {
  position: relative;
  width: 100%;
}
.iframeContainer iframe {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}
</style>
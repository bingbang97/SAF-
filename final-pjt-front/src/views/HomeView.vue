<template>
  <div id="hv">
    <main>
      <div v-if="this.$store.state.token">
        <NowPlayingMovie/>
        <br>
        <TopMovie/>
        <br>
        <TimeRelatedMovie/>
        <UserRecommendMovie/>
        <SsafyPlusRankMovie/>
      </div>
      <div v-if="!this.$store.state.token">
        <!-- <h1>로그인을 해주세요!</h1> -->
        <SafPlus/>
      </div>
    </main>
  </div>
</template>

<script>
import NowPlayingMovie from '@/components/NowPlayingMovie'
import TopMovie from '@/components/TopMovie.vue'
import TimeRelatedMovie from '@/components/TimeRelatedMovie'
import UserRecommendMovie from '@/components/UserRecommendMovie'
import SsafyPlusRankMovie from '@/components/SsafyPlusRankMovie'
import SafPlus from '@/components/SafPlus'

export default {
  name : 'HomeView',
  components:{
    NowPlayingMovie,
    TopMovie,
    TimeRelatedMovie,
    UserRecommendMovie,
    SsafyPlusRankMovie,
    SafPlus,
  },
}
</script>

<style scoped>
  
  #hv {
    width: 100%;
    place-items: center;
    background-color: rgb(3, 2, 10);
    /* background: linear-gradient(to top, #02000a 0%, #030157 100%); */
  }

</style>
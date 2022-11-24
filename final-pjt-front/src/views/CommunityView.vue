<template>
  <div id="cv">
    <div class="container">
      <ArticleList/>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'CommunityView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
    this.getComments()
  },
  methods: {
    getArticles(){
      if (this.isLogin){
        this.$store.dispatch('getArticles')
      } else{
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name : 'LogInView'})
      }
    },
    getComments(){
      this.$store.dispatch('getComments')
    },

  }
}
</script>

<style scoped>
  /* @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap'); */
  * {
    /* font-family: 'Nanum Gothic', sans-serif; */
    color: white
  }
  #cv{
    width: 100%;
    place-items: center;
    background: linear-gradient(to bottom, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);
    overflow-y: scroll;
    scrollbar-width: none;
    height: 100vh;
  }
  #cv::-webkit-scrollbar{
    display: none;

  }
</style>

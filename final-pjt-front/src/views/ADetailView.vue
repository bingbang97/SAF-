<template>
  <div id="cv">
    <div class="container">
      <div class="article">
        <div id="first">
          <div id="article-title">{{ article?.title }}</div>
          <div id="heart">
            <div v-if="userLikeArticle">
              <i class="bi bi-heart-fill" @click="likeArticle"></i>
            </div>
            <div v-else >
              <i class="bi bi-heart" @click="likeArticle"></i>
            </div>
          </div>
        </div>
        <div id="second">
          <div id="time">작성시간 : {{ new Date(article?.created_at).toLocaleString("ko-kr") }}</div>
        </div>
        <div class="content">
          <p id="article-content">{{ article?.content }}</p>
        </div>
        <div id="buttons">
          <div>
            <button 
              class="btn btn-light"
              @click="toCommunity"
            >목록</button>
          </div>
          <div>
            <button 
              type="button" class="btn btn-light"
              v-if="article?.user === this.$store.state.user.pk"
              @click="updateArticle"
            >수정</button>
            <button 
              type="button" class="btn btn-light"
              v-if="article?.user === this.$store.state.user.pk"
              @click="deleteArticle"
            ><i id="icon" class="bi bi-trash"></i></button>
          </div>
        </div>
        <hr>
        <ACommentCreateForm
        @commentSignal="renewComments"
        />
        <hr>
        <ACommentList
          :comments="comments"
          @completeUpdate="completeUpdate"
          @completeDelete="completeDelete"
        />
      </div>
    </div>  
  </div>
</template>

<script>
import ACommentList from '@/components/ACommentList'
import ACommentCreateForm from '@/components/ACommentCreateForm'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ADetailView',
  components: {
    ACommentList,
    ACommentCreateForm,
  },
  data() {
    return{
      article : null,
      comments : null,
      user : this.$store.state.user
    }
  },
  computed:{
    userLikeArticle(){
      let tmp = true
      if (this.article?.like_users.indexOf(this.user.pk) === -1)
        tmp = false
      return tmp
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail(){
      axios({
        method: 'get' ,
        url : `${API_URL}/api/v1/community/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((response) => {
        this.article = response.data
        // console.log(this.article)
        this.comments = response.data.comment_set
      })
      .catch((error)=>{console.log(error)})
    },
    renewComments(){
      this.getArticleDetail()
    },
    deleteArticle(){
      axios({
        method: 'delete',
        url : `${API_URL}/api/v1/community/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then(() => {
        // console.log(response)
        this.$router.push({ name : 'CommunityView'})

      })
      .catch((error) =>{
        console.log(error)
      })
    },
    updateArticle(){
      const article = this.article
      this.$router.push({ name : 'AUpdateView', params: { id : article.id } })

    },
    toCommunity(){
      this.$router.push({ name : 'CommunityView'})
    },
    completeUpdate(){
      this.getArticleDetail()
    },
    completeDelete(){
      this.getArticleDetail()
    },
    likeArticle(){
      axios({
        method: 'post',
        url : `${API_URL}/api/v1/community/${this.$route.params.id}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then(() => {
        this.getArticleDetail()
      })
      .catch((error) =>{
        console.log(error)
      })
    },
  },
}
</script>

<style scoped>
  * {
    color: black
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

  .container {
    margin-top:50px;
    margin-bottom:50px;
    border-radius: 5px;
    background-color: white;
    padding:15px
  }

  .article {
    padding: 10px;
  }

  .content {
    width:100%;
    height:relative;
  }
  #article-title {
    font-size: 25px;
    margin-bottom: 30px;
    
  }

  #article-content {
    font-size: 15px;
    margin-bottom: 30px;

  }

  #time {
    font-size: 12px;
    text-align: right;

  }

  i {
    color: red;
  }

  #icon {
    color: gray;
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

  #buttons {
    display: flex;
    justify-content: space-between;
    
  }

  #heart {
    float: right;
    margin-top: 8px;
    margin-right: 10px;
  }
  
  #first{
    display: flex;
    justify-content:space-between;
  }

  #second {
    display: flex;
    justify-content: right;
    margin:10px
  }

</style>

<template>
  <div id="all">
    <div id="user">{{ comment?.username }}</div>
      <div v-if="updateMode" >
        <ACommentUpdateForm 
          :comment="comment"
          @completeUpdate="completeUpdate"
        />
      </div>
      <div v-else>
        <div id="comment">
          <div id="content" v-if="!updateMode" >{{ comment?.content }}</div>
          <div>
            <button 
              type="button" class="btn btn-light"
              v-if="comment?.user === this.$store.state.user.pk"
              @click="toggleUpdateMode"
            >수정</button>
            <button 
              type="button" class="btn btn-light"
              v-if="comment?.user === this.$store.state.user.pk"
              @click="deleteComment"
            ><i class="bi bi-trash"></i></button>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import ACommentUpdateForm from '@/components/ACommentUpdateForm'

export default {
  name: 'ACommentListItem',
  components: {
    ACommentUpdateForm,
  },
  props: {
    comment: Object
  },
  data (){
    return {
      updateMode: false,
    }
  },
  computed:{
    article(){
      const id = this.$route.params.id
      let tmp = null
      this.$store.state.articles.forEach(article => {
        if(article.id === id){
          tmp = article
        }
      });
      return tmp
    }
  },  
  methods: {
    toggleUpdateMode() {
      this.updateMode = !this.updateMode
    },
    deleteComment () {
      axios({
        method: 'delete',
        url : `${API_URL}/api/v1/comments/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then(() => {
        this.$emit('completeDelete')
      })
      .catch((error) =>{
        console.log(error)
      })
    },
    completeUpdate(){
      this.updateMode = !this.updateMode
      this.$emit('completeUpdate')
    }
  }
}
</script>

<style scoped>
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

  #all {
    margin-bottom: 20px;
  }

  #comment {
    display: flex;
    justify-content: space-between;
    padding: 3px;
  }
  #user {
    font-weight: 600;
    padding: 1px 8px 1px 1px;
  }

  #content {
    padding: 3px;
  }

</style>
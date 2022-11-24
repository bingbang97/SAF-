<template>
  <div>
    <form @submit.prevent="updateComment" class="textbox">
      <input class="input-box" type="text" v-model="content">
      <button class="btn btn-light">완료</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ACommentUpdateForm',
  props: {
    comment: Object,
  },
  data(){
    return {
      content: null,
    }
  },
  created() {
    this.content = this.comment.content
  },
  methods: {
    updateComment(){
      const content = this.content
      axios({
        method: 'put' ,
        url : `${API_URL}/api/v1/comments/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content
        }
      })
      .then(() => {
        this.$emit('completeUpdate')
      })
      .catch((error)=>{console.log(error)})
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

  .input-box {
    width: 50px;
    margin: 7px;
    border-radius: 5px;
  }
  .textbox {
    position: relative;

    justify-content: left;
  }

  .textbox input[type="text"] {
    width: 90%; 
    height: 35px;  
    line-height : normal;  
    padding: .8em .5em; /* 원하는 여백 설정, 상하단 여백으로 높이를 조절 */
    font-family: inherit;  /* 폰트 상속 */
    border: 1px solid #999;
    border: none; 
    outline-style: none; 
    -webkit-appearance: none;  
    -moz-appearance: none;
    appearance: none;
    background-color: transparent;
  }

  .textbox input[type="text"]:hover {
    /* background: rgba(226, 226, 226, 0.1); */
    box-shadow: inset 4px 4px 60px 8px rgba(175, 175, 175, 0.2);
  }
  
  input::placeholder {
    font-size: 13px;
  }
</style>
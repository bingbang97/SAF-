<template>
  <form @submit.prevent="createComment" class="textbox">
    <input
      class="input-box"
      type="text"
      v-model="content"
      placeholder="댓글을 작성하세요"
    >
    <button type="submit" class="btn btn-light">작성</button>
  </form>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ACommentCreateForm',
  data () {
    return {
      content: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content
      axios ({
        method:'post',
        url: `${API_URL}/api/v1/community/${this.$route.params.id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content,
        }
      })
      .then(() => {
        this.$emit('commentSignal')
        this.content = null
      })
      .catch((error) => {
        console.log(error)
      })

    }
  },
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
    padding: .8em .5em; 
    font-family: inherit;
    border: 1px solid #999;
    border: none; 
    outline-style: none; 
    -webkit-appearance: none;  
    -moz-appearance: none;
    appearance: none;
    background-color: transparent;
  }

  .textbox input[type="text"]:hover {
    box-shadow: inset 4px 4px 60px 8px rgba(175, 175, 175, 0.2);
  }
  
  input::placeholder {
    font-size: 13px;
  }
</style>
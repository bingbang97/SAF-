<template>
  <div id="acv">
  <div class="container">
    <form @submit.prevent="createArticle">
    <div class="title">게시글 작성</div>
      <div class="input-box">
        <input type="text" id="title" placeholder="Title" v-model="title" required>
        <hr>
      </div>
      <div>
        <textarea cols="30" rows="10" id="content" placeholder="Content" v-model="content" required></textarea>
        <hr>
      </div>
      <div class="input-box">
        <div class="underline"></div>
        <input type="submit" value="글 쓰기">
      </div>

    </form>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ACreateView',
  data() {
    return{
      title:null,
      content:null,
    }
  },
  methods: {
    createArticle(){
      const title = this.title
      const content = this.content
      if (!title){
        alert('제목을 입력해주세요')
        return
      }
      else if (!content){
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/community/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data:{
          title,
          content,
        }
      })
      .then(() =>{
        this.$router.push({ name : 'CommunityView'})
      })
      .catch((error) =>{
        console.log(error)
      })
      
    }
  }
}
</script>

<style scoped>

  *{
    margin:0;
    padding:0;
    box-sizing:border-box;

  }

  #acv {
    display: grid;
    height: 100vh;
    width: 100%;
    place-items: center;
    background: linear-gradient(to bottom, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);
  }

  .container {
    background: #fff;
    max-width: 700px;
    min-width: 200px;
    width: 50vw;
    padding: 25px 30px;
    border-radius: 5px;
    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.15);

  }

  .container form .title {
    font-size: 30px;
    font-weight: 600;
    margin: 20px 0 10px 0;
  }

  .container form .input-box {
    width: 100%;
    height: 45px;
    margin-top: 25px;
    position: relative;
  }

  .container form .input-box input {
    height: 100%;
    width: 100%;
    outline: none;
    font-size: 16px;
    border: none;
  }
  .container form textarea {
    margin-top: 25px;
    width: 100%;
    outline: none;
    font-size: 16px;
    border: none;
    position: relative;
  }

  .container form .input-box input[type="submit"] {
    font-size: 17px;
    color:#fff;
    border-radius: 5px;
    cursor: pointer;
    background: linear-gradient(to bottom, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);
    transition: all 0.3s ease;
  }

  .container form .input-box input[type="submit"]:hover {
    letter-spacing: 1px;
    background: linear-gradient(to top, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);

  }

  span {
    font-size: 12px;
    color: lightslategray;
  }
</style>
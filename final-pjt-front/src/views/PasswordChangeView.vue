<template>
  <div id="pc">
    <div class="container">
    <form @submit.prevent="changePassword">
      <div class="input-box">
        <input type="password" id="old_password" placeholder="Enter your password" v-model="old_password" required>
        <div class="underline"></div>
      </div>
      <div class="input-box">
        <input type="password" id="new_password1" placeholder="Enter your new password" v-model="new_password1" required>
        <div class="underline"></div>
      </div>
      <div class="input-box">
        <input type="password" id="new_password2" placeholder="Confirm your new password" v-model="new_password2" required>
        <div class="underline"></div>
      </div>
      <div class="input-box">
        <input type="submit" value="Change Password">
      </div>
    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PasswordChangeView',
  data(){
    return{
      new_password1 : null,
      new_password2 : null,
      old_password : null,
    }
  },
  methods:{
    changePassword(){
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
      const old_password = this.old_password
      axios({
        method: 'post',
        url : `${API_URL}/accounts/password/change/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data:{
          new_password1,
          new_password2,
          old_password,
        }
      })
      .then(() =>{
        this.$router.push({name: 'HomeView'})
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

  #pc {
    display: grid;
    height: calc(100vh - 64.422px);
    width: 100%;
    place-items: center;
    background: linear-gradient(to bottom, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);
  }

  .container {
    background: #fff;
    max-width: 500px;
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

  .container form .underline {
    position: absolute;
    content:'';
    height: 2px;
    width: 100%;
    background: #ccc;
    left:0;
    bottom:0;
  }
  
  .container form .underline:after{
    position: absolute;
    content: '';
    height:2px;
    width: 100%;
    left:0;
    bottom:0;
    background: linear-gradient(to right, #06001b 0%, #030157 100%); 
    transform : scaleX(0);
    transform-origin: left;
    transition: all 0.3s ease;
  }

  .container form .input-box input:focus ~ .underline:after,
  .container form .input-box input:valid ~ .underline:after{
    transform : scaleX(1);
    transform-origin: left;
  }


  .container form .input-box input[type="submit"] {
    font-size: 15px;
    color:#fff;
    border-radius: 5px;
    cursor: pointer;
    background: linear-gradient(to bottom, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);
    transition: all 0.3s ease;
  }

  .container form .input-box input[type="submit"]:hover {
    letter-spacing: 1px;
    background: linear-gradient(to left, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);

  }

  .selectbox {
    display: flex;
    justify-content: space-evenly;
    
  }

  select {
    width: 100%;
    height: 50px;
    border-radius: 3px;
    border: 1px solid #bfbfbf;
    margin-left: 10px;
    margin-right: 10px;
  }

  select:focus,
  select:valid {
        border: 1px solid #06001b;
        outline: none;
  }

  span {
    font-size: 12px;
    color: lightslategray;
  }
</style>
<template>
  <div id="bc">
    <div class="container">
      <form @submit.prevent="logIn">
        <div class="title">Login</div>
        <div class="input-box">
          <input type="text" id="username" placeholder="Enter your username" v-model="username" required>
          <div class="underline"></div>
        </div>
          
        <div class="input-box">              
          <input type="password" id="password" placeholder="Enter your password" v-model="password" required>
          <div class="underline"></div>
          <div v-if="isAuthError"> 
            <span v-for="(error, idx) in nonFieldError" :key="idx">{{ error }}</span> 
          </div>
        </div>

      
        <div class="input-box"> 
          <input type="submit" value="LogIn">
        </div>
<!-- 
          <div class="errorbox" v-if="isAuthError">
            <div>{{ authError }}</div>      
          </div> -->
        <div id="already">
          <span>Don't you have an account yet?</span>
          <span id="tosignup" @click="toSignUp"> SIgn Up</span>
        </div>
      </form>
    </div>
  </div>
  
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'LogInView',
  data() {
    return{
      username: null,
      password: null,
      usernameError: null,
      passwordError: null,
      nonFieldError: null,
    }
  },
  computed: {
      ...mapGetters(['isAuthError']),
      ...mapGetters(['authError'])
  },
  methods: {
    logIn(){
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password
      }
      this.$store.dispatch('logIn', payload)
      // this.$router.push({ name: 'HomeView' })
      this.saveError()
    },
    saveError(){
      if (this.isAuthError){
        // console.log(this.authError)
        this.nonFieldError = this.authError.non_field_errors
        this.usernameError = this.authError.username
        this.passwordError = this.authError.password
      }
    },
    toSignUp(){
      this.$router.push({ name: 'SignUpView' })
    }
  },
}
</script>

<style scoped>

  *{
    margin:0;
    padding:0;
    box-sizing:border-box;

  }

  #bc {
    display: grid;
    height: calc(100vh - 64.422px);
    width: 100%;
    place-items: center;
    background: linear-gradient(to bottom, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%);
  }

  .container {
    background: #fff;
    max-width: 400px;
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
    background: linear-gradient(to right, rgb(3, 2, 10) 0%, rgb(1, 0, 36) 100%); 
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

  span {
    font-size: 12px;
    color: lightslategray;
    margin-right: 3px;
  }

  #tosignup{
    color: rgb(3, 2, 10);
  }

  #tosignup:hover {
    text-decoration: underline;

  }

  #already {
    margin-top: 8px;
    margin-left: 4px;
    display: flex;
    justify-content: center;
  }
</style>

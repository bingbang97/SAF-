<template>
  <div id="bc">
    <div class="container">
      <form @submit.prevent="signUp">
          <div class="title">Sign Up</div>

          <div class="input-box">
            <input type="text" id="username" placeholder="Enter your username" v-model="username" required>
            <div class="underline"></div>
            <div v-if="isAuthError"> 
              <span v-for="(error, idx) in usernameError" :key="idx">{{ error }}</span> 
            </div>
          </div>
          <div class="input-box">
            <input type="password" id="password1" placeholder="Enter your password" v-model="password1" required>
            <div class="underline"></div>            
            <div v-if="isAuthError"> 
              <span v-for="(error, idx) in password1Error" :key="idx">{{ error }}</span> 
            </div>
          </div>

          <div class="input-box">
            <input type="password" id="password2" placeholder="Confirm your password" v-model="password2" required>
            <div class="underline"></div>
            <div v-if="isAuthError"> 
              <span v-for="(error, idx) in password2Error" :key="idx">{{ error }}</span> 
            </div>
          </div>
          <br>

          <div class="selectbox">
            <select v-model="like_genre1" id="like_genre1">
              <option value="">--choose a genre--</option>
              <option value="Adventure">Adventure</option>
              <option value="Fantasy">Fantasy</option>
              <option value="Animation">Animation</option>
              <option value="Drama">Drama</option>
              <option value="Horror">Horror</option>
              <option value="Action">Action</option>
              <option value="Comedy">Comedy</option>
              <option value="History">History</option>
              <option value="Western">Western</option>
              <option value="Thriller">Thriller</option>
              <option value="Crime">Crime</option>  
              <option value="Documentary">Documentary</option>
              <option value="Science Fiction">Science Fiction</option>
              <option value="Mystery">Mystery</option>
              <option value="Music">Music</option>
              <option value="Romance">Romance</option>
              <option value="Family">Family</option>
              <option value="War">War</option>
              <option value="TV Movie">TV Movie</option>
            </select>
            <!-- <div v-if="isAuthError"> 
              <span v-for="(error, idx) in like_genre1Error" :key="idx">{{ error }}</span> 
            </div>
            <br v-else> -->
            <br>

            
            <select v-model="like_genre2" id="like_genre2">
              <option value="">--choose a genre--</option>
              <option value="Adventure">Adventure</option>
              <option value="Fantasy">Fantasy</option>
              <option value="Animation">Animation</option>
              <option value="Drama">Drama</option>
              <option value="Horror">Horror</option>
              <option value="Action">Action</option>
              <option value="Comedy">Comedy</option>
              <option value="History">History</option>
              <option value="Western">Western</option>
              <option value="Thriller">Thriller</option>
              <option value="Crime">Crime</option>  
              <option value="Documentary">Documentary</option>
              <option value="Science Fiction">Science Fiction</option>
              <option value="Mystery">Mystery</option>
              <option value="Music">Music</option>
              <option value="Romance">Romance</option>
              <option value="Family">Family</option>
              <option value="War">War</option>
              <option value="TV Movie">TV Movie</option>
            </select>
            <!-- <div v-if="isAuthError"> 
              <span v-for="(error, idx) in like_genre2Error" :key="idx">{{ error }}</span> 
            </div>
            <br v-else> -->
            <br>

            
            <select v-model="like_genre3" id="like_genre3">
              <option value="">--choose a genre--</option>
              <option value="Adventure">Adventure</option>
              <option value="Fantasy">Fantasy</option>
              <option value="Animation">Animation</option>
              <option value="Drama">Drama</option>
              <option value="Horror">Horror</option>
              <option value="Action">Action</option>
              <option value="Comedy">Comedy</option>
              <option value="History">History</option>
              <option value="Western">Western</option>
              <option value="Thriller">Thriller</option>
              <option value="Crime">Crime</option>  
              <option value="Documentary">Documentary</option>
              <option value="Science Fiction">Science Fiction</option>
              <option value="Mystery">Mystery</option>
              <option value="Music">Music</option>
              <option value="Romance">Romance</option>
              <option value="Family">Family</option>
              <option value="War">War</option>
              <option value="TV Movie">TV Movie</option>
            </select>
            <!-- <div v-if="isAuthError"> 
              <span v-for="(error, idx) in like_genre3Error" :key="idx">{{ error }}</span> 
            </div>
            <br v-else> -->
            <br>
          </div>
          <div v-if="like_genre1Error || like_genre2Error || like_genre3Error">
            <span>Genre fields may not be null!</span>
          </div>
          <div class="input-box">
            <input type="submit" value="SignUp">
          </div>
          <div id="already">
            <span>Already have an account</span><span id="toLogin" @click="toLoginView">LogIn</span>
          </div>
        </form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
  name: 'SignUpView',

  computed: {
      ...mapGetters(['isAuthError']),
      ...mapGetters(['authError'])
  },

  data() {
    return{
      username: null,
      password1: null,
      password2: null,
      like_genre1: null,
      like_genre2: null,
      like_genre3: null,

      usernameError : null,
      password1Error: null,
      password2Error: null,
      like_genre1Error: null,
      like_genre2Error: null,
      like_genre3Error: null,
    }
  },
  methods: {
    signUp(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const like_genre1 = this.like_genre1
      const like_genre2 = this.like_genre2
      const like_genre3 = this.like_genre3

      const payload = {
        username,
        password1,
        password2,
        like_genre1,
        like_genre2,
        like_genre3,
      }
      this.$store.dispatch('signUp', payload)
      // this.$router.push({ name: 'HomeView' })
      this.saveError()
    },
    saveError(){
      if (this.isAuthError){
        console.log(this.authError)
        this.usernameError = this.authError.username
        this.password1Error = this.authError.password1
        this.password2Error = this.authError.non_field_errors
        this.like_genre1Error = this.authError.like_genre1
        this.like_genre2Error = this.authError.like_genre2
        this.like_genre3Error = this.authError.like_genre3
      }
    },
    toLoginView () {
      this.$router.push({ name: 'LogInView' })
    }
  },
  mounted(){
    this.saveError()
  }
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
    background: linear-gradient(to bottom, #030209 0%, rgb(1, 0, 36) 100%);
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
        border: 1px solid rgb(3, 2, 10);
        outline: none;
  }

  span {
    font-size: 12px;
    color: lightslategray;
    margin-right: 3px;
  }

  #toLogin{
    color: rgb(3, 2, 10);
  }

  #toLogin:hover {
    text-decoration: underline;
  }

  #already {
    margin-top: 8px;
    margin-left: 4px;
    display: flex;
    justify-content: center;
  }
</style>

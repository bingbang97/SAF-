<template>
  <div>
    <div id="bc">
      <form @submit.prevent="createMComment" class="textbox">
        <star-rating :star-size="20" :increment="0.5" v-model="vote_rate" :show-rating="false"></star-rating>
        <input
          class="input-box"
          type="text"
          v-model="content"
          placeholder="한줄평"
        >
        <input id="btn" type="submit" value="작성">
      </form>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MCommentCreateForm',
  data () {
    return {
      vote_rate: 0,
      content: null,
    }
  },
  components: {
    StarRating
  },
  methods: {
    createMComment() {
      const vote_rate = this.vote_rate
      const content = this.content
            
      axios ({
        method:'post',
        url: `${API_URL}/movies/movie/${this.$route.params.id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          vote_rate,
          content,
        }
      })
      .then(() => {
        this.$emit('commentSignal')
        this.content = null
        this.vote_rate = 0
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
}
</script>

<style scoped>
  #btn {
    position: relative;
    padding: 3px 10px;
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
    background-color: rgb(185, 185, 185);
    color: rgb(95, 95, 95);

  }

  .input-box {
    width: 50px;
    margin: 7px;
    border-radius: 5px;
  }
  .textbox {
    position: relative;
    display: flex;
    justify-content: left;
  }

  .textbox input[type="text"] {
    width: 435px; 
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
    color: rgb(153, 153, 153);
    box-shadow: inset 4px 4px 60px 8px rgba(175, 175, 175, 0.2);
  }

  input::placeholder {
    font-size: 13px;
    color: rgb(153, 153, 153);
  }

  #bc {
    width: 70vw;
    max-width: 600px;
  }
</style>
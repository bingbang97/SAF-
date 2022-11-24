<template>
<div id="app">
  <nav>
    <div id="nav">
      <img id="image" src="@/assets/navlogo.png" alt="" @click="toHomeView">
      <router-link :to="{ name: 'HomeView' }">Home</router-link>
      <router-link :to="{ name: 'CommunityView' }">Community</router-link>
    </div >
    <div id="nav" v-if="!this.$store.state.token">
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link>
      <router-link :to="{ name: 'LogInView' }">LogIn</router-link>
    </div>
    <div v-else id="nav">
      <router-link :to="{ name: 'ProfileView', params:{ id: `${user?.pk}`} }">My Profile</router-link>
      <a id="logout" @click="logOut">Logout</a>
    </div>
  </nav>
  <div id="rv">
    <router-view/>
  </div>

</div>
</template>

<script>


export default {
  name: 'App',
  methods:{
    logOut(){
      this.$store.dispatch('logOut')
    },
    toHomeView () {
      this.$router.push({ name: 'HomeView' })
    }
  },
  computed: {
    user(){
      return this.$store.state.user
    }
  },
  
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
  #rv {
    width: 100%;
    background-color: rgb(3, 2, 10);
    /* background: linear-gradient(to top, rgb(6, 0, 26) 0%, rgb(3, 1, 87) 100%); */
    overflow: auto;
    font-family: 'Lato', sans-serif;

  }
  
  nav {
    padding: 20px;
    background-color: rgb(3, 2, 10);
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    width: 100%;
    z-index: 99999;
  }


  nav a {
    position: relative;
    text-decoration: none;
    font-size: 15px;
    text-transform: capitalize;
    color: #909090;

    padding:0 5px;
    margin: 5px;
  }

  nav a:hover {
    color :white;

  }

  nav a:hover::before {
    width: 100%;
  }

  nav a.router-link-exact-active {
    color: #ffffff;
  }
  nav a.router-link{
    color: #ffffff;
  }

  /* logout 만 a태그 적용이 안되서 반복.. */
  #logout {
    position: relative;
    text-decoration: none;
    font-size: 15px;
    text-transform: capitalize;
    color: #909090;

    padding:0 1px;
    margin: 5px;
  }

  #logout:hover {
    color :white;

  }

  #logout:hover::before {
    width: 100%;
  }

  #logout.router-link-exact-active {
    color: #ffffff;
  }
  #logout.router-link{
    color: #ffffff;
  }

  #image {
    width:40px;
    height: relative;
    margin-right : 7px
  }
  

</style>



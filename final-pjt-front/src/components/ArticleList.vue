<template>
  <div class="container">
    <div id="header">
      <span id="titie">FREEBOARD</span>
      <i id="submit-button" class="bi bi-pencil-square btn btn-outline-secondary" type="button" @click="toCreate"></i>
    </div>
    <div>
      <table class="table">
        <thead>
        <tr class="grid">
          <th  class="col-md-5">제목</th>
          <th class="col-md-1">작성자</th>
          <th class="col-md-2">날짜</th>
        </tr>
        </thead>
        <tbody>
          <tr v-for="article in articles" :key="article.id">
            <td id="tabletitle">
              <router-link 
              :to="{ name : 'ADetailView', params : { id: article.id } }"
              >
                {{ article.title }}
              </router-link>
            </td>
            <td>
              <router-link :to="{ name: 'ProfileView', params:{ id: `${article.user}`} }">{{ article.username }}</router-link>
              
              </td>
            <td>{{ new Date(article.created_at).toLocaleDateString("ko-kr", { weekday: "long", year: "numeric", month: "short", day: "numeric",}) }}</td>
          </tr>
        </tbody>
      </table>
    </div>


  </div>
</template>

<script>


export default {
  name: 'ArticleList',
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods: {
    toCreate(){
      this.$router.push({ name : 'ACreateView'})
    },
  }
}
</script>

<style scoped>

  .container {
    /* margin: 50px; */
    max-width: 1000px;
    margin-top: 50px;
    margin-bottom: 50px;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.15);
    padding: 20px;
  }
  .table{
    max-width: 1000px;
    color: black;
    text-align: center;
    font-size: 13px;
  }
  tbody tr:hover{
    color: lightslategray
  }
  tbody tr:hover a{
    color: lightslategray;
    text-decoration: none;

  }
  
  #submit-button {
    margin-top: 13px;
    margin-right: 2px;

  }
  .table a{
    color: black;
    text-decoration: none;
  }

  .container span {
    /* float: left; */
    color: black;
    margin: 15px;
    
  }

  #header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
  }
  
  #tabletitle {
    text-align: left;
  }
  
  
</style>

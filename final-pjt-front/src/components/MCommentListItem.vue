<template>
  <div id="bc">
    <div id="omcl">
      <div id="mcl">
        <star-rating id="st" 
        :rating="comment?.vote_rate" 
        :read-only="true" 
        :star-size="20"
        :show-rating="false"
        :increment="0.5"
        >
        </star-rating> 
        <span>{{ comment?.content }}</span>
      </div>
    <span id="cu">{{ comment?.username }}</span>
    <span id="cca">{{ new Date(comment?.created_at).toLocaleString("ko-kr") }}</span>
    <!-- <hr> -->
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
export default {
  name: 'MCommentListItem',
  props: {
    comment:Object
  },
  components: {
    StarRating
  },
}
</script>

<style scoped>
  #bc {
    width: 70vw;
    max-width: 600px;
  }

  #omcl{
    padding-top:15px;
    padding-bottom:15px;
    
  }
  #mcl{
    display: flex;
    justify-content: left;
    
  }
  #mcl span{
    font-size: 17px;
    margin-top: 4px;
  }
  #st{
    margin-right: 10px;
  }
  #cu{
    margin-left: 110px;
    font-size: 12px;
    font-weight: bold;
  }
  #cca{
    margin-left: 10px;
    font-size: 12px;
  }
  
</style>
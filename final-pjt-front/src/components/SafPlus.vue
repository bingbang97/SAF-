<template>
  <div id="sp">
    <!-- <img class="circle-img" src="@/assets/circle.png" alt=""> -->
    <img class="logo-img" src="@/assets/logoend.png" alt="">
  </div>
</template>

<script>
export default {
  name:'SafPlus',
}
</script>

<style scoped>
  *{
    margin:0;
    padding:0;
    box-sizing:border-box;

  }

  #sp {
    display: grid;
    height:calc(100vh - 64.422px);
    width: 100%;
    place-items: center;
    background: linear-gradient(to bottom, #030209 0%, rgb(1, 0, 36) 100%);
  }
  .logo-img{

    height: 400px;
  }
  /* .circle-img{
    visibility: hidden;
  }
  #sp:hover .circle-img{
    visibility: visible;
    background: linear-gradient(to rigth, #2600ff 100%, rgb(255, 255, 255) 100%);
  } */

</style>
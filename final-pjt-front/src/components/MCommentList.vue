<template>
  <div>
    <MCommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import MCommentListItem from '@/components/MCommentListItem'
export default {
  name: 'MCommentList',
  components: {
    MCommentListItem,
  },
  props: {
    comments:Array
  }
}
</script>

<style>

</style>
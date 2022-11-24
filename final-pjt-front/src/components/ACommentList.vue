<template>
  <div>
    <ACommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      @completeUpdate="completeUpdate"
      @completeDelete="completeDelete"
    />
  </div>
</template>

<script>
import ACommentListItem from '@/components/ACommentListItem'

export default {
  name: 'ACommentList',
  components: {
    ACommentListItem,
  },
  props: {
    comments:Array
  },
  methods: {
    completeUpdate(){
      this.$emit('completeUpdate')
    },
    completeDelete(){
      this.$emit('completeDelete')
    }
  }

}
</script>

<style >

</style>
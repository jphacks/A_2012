<template>
  <div class="baloon">
    {{ sentence }}
  </div>
</template>

<script>
export default {
  name: "Fukidashi",
  props: {
    sentence: String,
  },
};
</script>

<style scoped>
.baloon {
  border: solid 0.2rem;
  border-color: #666;
  height: auto;
  position: relative;
  padding: 2rem;
  background-color: #f7f7f7;
  color: #000000;
  border-radius: 8rem;
}
</style>
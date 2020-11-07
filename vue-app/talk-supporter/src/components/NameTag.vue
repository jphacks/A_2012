<template>
  <span class="member" :style="styles">{{ member }}</span>
</template>

<script>
export default {
  name: "NameTag",
  props: {
    member: String,
    color: String,
  },
  computed: {
      styles () {
          return {
              '--bgcolor': this.color,
          }
      }
  }
};
</script>

<style scoped>
.member {
  border-radius: 1.75rem;
  font-size: .5rem;
  margin: 2rem 0.5rem;
  padding: .2rem 1rem;
  color: #ffffff;
  --bgcolor: #0066FF;
  background-color: var(--bgcolor);
}
</style>
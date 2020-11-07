<template>
  <button>{{ btnLabel }}</button>
</template>

<script>
export default {
  name: "NMButton",
  props: {
    btnLabel: String,
  },
};
</script>
<style scoped>
button {
  width: 80%;
  color: #ffa200;
  margin: 1rem 0rem;
  margin-bottom: 2rem;
  padding: 0.5rem 0rem;
  border-radius: 3.5rem;
  background: #f7f7f7;
  box-shadow: 1rem 0.5rem 1rem #d2d2d2, -1rem -0.5rem 1rem #ffffff;
}
button{
  outline: none;
}
</style>
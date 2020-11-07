<template>
  <div class="card">
    <h1 class="text card-title">{{ title }}</h1>
    <div class="example-wrapper">
      <p class="topic-detail" v-for="example in examples" :key="example.index">
        {{ example }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "NMTopicCard",
  props: {
    title: String,
    examples: Array,
  },
};
</script>

<style scoped>
.card {
  width: 100%;
  margin: 2rem 0rem;
  padding: 2.5rem 1rem;
  border-radius: 30px;
  background-color: #f7f7f7;
  box-shadow: 1rem 1rem 1rem #d2d2d2, -1rem -1rem 1rem #ffffff;
  height: 25rem;
}
.example-wrapper {
  margin-top: 2rem;
}
h1,
p {
  color: #ffa200;
}
.topic-detail {
  color: black;
  margin: 1rem;
}
</style>
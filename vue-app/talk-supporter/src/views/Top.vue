<template>
  <div>
    <h1>話題提供マン</h1>
    <img class="logo" src="../assets/logo.png" alt="" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- <div class="card-wrapper">
    <NMTopicCard title="ルーム作成" :examples="newsList" />
  </div> -->
    <div class="btn-wrapper">
      <NMButton btnLabel="話題セット" v-on:click="movePage('set')" />
      <NMButton btnLabel="会話を始める" v-on:click="movePage('start')" />
      <NMButton btnLabel="会話に参加する" v-on:click="movePage('join')" />
      <NMButton btnLabel="今までの会話" v-on:click="movePage('history')" />
    </div>
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import NMButton from "../components/NMButton.vue";
import "ress";
import router from "../router/index.js";

export default {
  name: "Top",
  components: {
    NMButton,
  },
  methods: {
    movePage: function (target) {
      router.push(target);
    },
  },
};
</script>

<style>
body {
  /* padding: 3rem 6rem; */
}
.btn-wrapper {
  margin-top: 5rem;
  padding: 0rem 3rem;
}
* {
  background-color: #f7f7f7;
}
.card-wrapper {
  padding: 1rem;
}
#app {
  text-align: center;
}
.logo {
  margin-top: 3rem;
}
</style>

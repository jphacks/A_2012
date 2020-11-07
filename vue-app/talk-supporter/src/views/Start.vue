<template>
  <div>
    <div class="card">
      <h5 class="text card-title">ルームを作成する</h5>
      <form action="" name="form">
        <input
          class="textbox"
          id="room-name"
          name="subjectname"
          type="text"
          placeholder="例)JPHACKS2020打ち上げ"
        />
      </form>
      <NMButton btnLabel="ルームを作成" v-on:click="makeRoom()" />
    </div>
  </div>
</template>

<script>
import NMButton from "../components/NMButton";
import router from "../router/index.js";
import "ress";

export default {
  name: "Top",
  components: {
    NMButton,
  },
  methods: {
    makeRoom: function () {
        const roomName = document.getElementById('room-name').value;
        console.log(roomName);
        router.push('/talk')
    },
  },
};
</script>

<style scoped>
* {
  font-size: 1.2rem;
}
.card {
  width: 100%;
  margin: 5rem 0rem;
  padding: 2.5rem 1rem;
  border-radius: 30px;
  background-color: #f7f7f7;
  box-shadow: 1rem 1rem 1rem #d2d2d2, -1rem -1rem 1rem #ffffff;
}
.card-title {
  font-weight: normal;
  color: #ffa200;
}
.textbox {
  background-color: #f7f7f7;
  margin: 5rem 0rem;
  width: 100%;
  border-radius: 10px;
  box-shadow: inset 0.5rem 0.5rem 0.5rem #d2d2d2,
    inset -0.5rem -0.5rem 0.5rem #ffffff;
  padding: 1rem 0.5rem;
}
</style>
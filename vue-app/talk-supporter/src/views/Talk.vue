<template>
  <div>
    <div class="card">
      <h2>{{ RoomName }}</h2>
    </div>
    <!-- <div class="tab"></div> -->
    <!-- <div class="projection3">
        <p class="topic_name"><em>雑談ルーム</em></p>
        <p class="name">メンバー</p>
        <span class="member">fuchio</span>
        <span class="member">草原</span>
        <span class="member">ddsk</span>
      </div> -->
    <NMButton id="btn" btnLabel="会話を始める" />
    <div id="canvas-container">
      <canvas id="sincanvas" class="room_canvas"></canvas>
      <Fukidashi
        sentence="最近、キーボード一体型のラズベリーパイが発売されましたね。"
      />
    </div>
    <NMButton class="finish-btn" btnLabel="会話を終了" />
  </div>
</template>
<script>
import Fukidashi from "../components/Fukidashi.vue";
import NMButton from "../components/NMButton.vue";
import "ress";
// import router from "../router/index.js";

export default {
  name: "Talk",
  components: {
    Fukidashi,
    NMButton,
  },
  data(){
      return{
          RoomName: 'JPHACKS2020開発'
      }
  }
};

window.addEventListener("load", draw, false);
function draw() {
  var r = 5;
  var T = 300;
  var degree = 0;

  var canvas = document.getElementById("sincanvas");
  var ctx = canvas.getContext("2d");

  function loop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();

    ctx.strokeStyle = "#0000FF";
    ctx.lineWidth = 1;
    drawWave(degree);

    ctx.stroke();

    ctx.fillStyle = "#0000FF";
    ctx.globalAlpha = 1;
    ctx.lineTo(canvas.width, canvas.height);
    ctx.lineTo(0, canvas.height);
    ctx.closePath();
    ctx.fill();

    degree += 3;

    requestAnimationFrame(loop);
  }

  loop();

  function drawWave(degree) {
    ctx.moveTo(
      0,
      -r * Math.sin(((2 * Math.PI) / T) * degree) + canvas.height / 2
    );
    for (var x = 1; x <= canvas.width; x += 1) {
      var y = -r * Math.sin(((2 * Math.PI) / T) * (degree + x));
      ctx.lineTo(x, y + canvas.height / 2 +70); //min,max+-70
    }
  }
}

// ネガポジの履歴
let queue = [];

// ネガティブに話題が寄った時に実行される関数
const alertNegative = () => {
  queue.splice(0);
  console.log("話題代えよ");
};

// 感情分析API
const fetchSentiJudge = async (url) => {
  const resp = await fetch(url);
  const judge = await resp.json();
  console.log(judge.emotion);
  if (queue.length == 8) {
    queue.shift();
    queue.push(judge.emotion);
    if (queue.every((value) => value == "negative")) {
      alertNegative();
    }
  } else {
    queue.push(judge.emotion);
  }
};

// 音声認識API
const speech = new SpeechRecognition.SpeechRecognition()();
speech.lang = "ja-JP";

const btn = document.getElementById("btn");

btn.addEventListener("click", function () {
  speech.start();
});

fetchSentiJudge('aaa')

speech.onresult = function (e) {
  speech.stop();
  if (e.results[0].isFinal) {
    var autotext = e.results[0][0].transcript;
    var chunk = autotext.replace(/\s/g, "");
    var url = "http://127.0.0.1:5000/?s=" + chunk;
    fetchSentiJudge(url);
  }
};

speech.onend = () => {
  speech.start();
};
</script>

<style scoped>
body {
  background: #ffffff;
  text-align: center;
}
.tab {
  background-color: #ffa200;
  height: 8rem;
}
.member {
  border-radius: 1.75rem;
  font-size: 1.5rem;
  margin: 2rem 0.5rem;
  padding: 0.5rem 2rem;
  background-color: red;
  color: #ffffff;
}
.name {
  font-size: 2rem;
}
.topic_name {
  margin: 0.5rem 0rem;
  font-size: 3.5rem;
}
.room_canvas {
  border: solid 0.3rem;
  border-color: #666;
  border-radius: 15rem;
  height: 15rem;
  width: 15rem;
  /* margin-top: 5rem; */
  margin-bottom: 2rem;
}
.finish-btn {
  margin-top: 3rem;
}
.card {
  width: 100%;
  /* margin: 5rem 0rem; */
  margin-top: 3rem;
  margin-bottom: 4rem;
  padding: 2.5rem 1rem;
  border-radius: 30px;
  background-color: #f7f7f7;
  box-shadow: 1rem 1rem 1rem #d2d2d2, -1rem -1rem 1rem #ffffff;
}
</style>
// 最後まで行ってから戻ると、興味あるなしのボタン押せなくなる
// やっぱ興味ないって思って戻って興味ない押してもお気に入り配列からは消えない
<template>
  <div>
    <NMTopicCard :title="current.title" :examples="current.examples" />
    <NMButton
      class="fav-btn"
      id="unfav"
      btnLabel="興味ない"
      v-on:click="nextTopic()"
      :disabled="isDisable"
    />
    <NMButton
      class="fav-btn"
      id="fav"
      btnLabel="興味ある"
      v-on:click="favorite(current.title)"
      :disabled="isDisable"
    />
    <div>
      <p id="progress">{{ currentId }}/7</p>
    </div>
    <div>
      <NMButton
        class="paging"
        id="back"
        btnLabel="◀"
        v-on:click="prevTopic()"
      />
      <NMButton
        class="paging"
        id="prog"
        btnLabel="▶"
        v-on:click="nextTopic()"
      />
    </div>
      <NMButton
        id="backTop"
        btnLabel="TOPへ戻る"
        v-on:click="backTop()"
      />
  </div>
</template>

<script>
import NMTopicCard from "../components/NMTopicCard.vue";
import NMButton from "../components/NMButton.vue";
import "ress";
import router from "../router/index.js";

export default {
  name: "Set",
  components: {
    NMButton,
    NMTopicCard,
  },
  methods: {
    favorite: function (favTopic) {
      this.nextTopic();
      this.favTopics.push(favTopic);
      console.log(this.favTopics);
    },
    nextTopic: function () {
      this.currentId++;
      if (this.currentId == 8) {
        this.isDisable = true;
      }
    },
    prevTopic: function () {
      this.currentId--;
    },
    backTop: function () {
      router.push("/");
    },
  },
  data() {
    return {
      isDisable: false,
      favTopics: [],
      currentId: 1,
      list: [
        {
          id: 1,
          title: "エンタメ",
          examples: [
            "ベッキー 新居は3億円豪邸? - auone.jp",
            '"あざとキング"Sexy Zone中島健人に田中みな実脱帽「あざといピラミッドの頂点」 - モデルプレス',
            "ガンダム：リ・ガズィ・カスタムがMETAL ROBOT魂に 「逆襲のシャア MSV」のリ・ガズィの発展機 - MANTANWEB",
          ],
        },
        {
          id: 2,
          title: "ジェネラル",
          examples: [
            "J2新潟社長の引責辞任で問われる棚上げ状態のJ1仙台責任問題（THE PAGE） - Yahoo!ニュース",
            "芸能事務所でクラスター、女性タレント１０人感染…屋内でライブ活動 - 読売新聞",
            "バイデン氏 過半数へ優勢強まる トランプ氏「絶対諦めない」 - 日本経済新聞",
          ],
        },
        {
          id: 3,
          title: "ヘルス",
          examples: [
            "予防接種中断：はしか・ポリオ流行のおそれ【プレスリリース】 - ストレートプレス",
            "【乾燥対策】エアコンや加湿器だけではない⁉ ３つのエコ加湿でお部屋の乾燥防止！ - マイナビニュース",
            "ANA、アバター×ドローン「遠隔医療」を五島市で成功--ドコモ、長崎大学、ACSLらと - CNET Japan",
          ],
        },
        {
          id: 4,
          title: "サイエンス",
          examples: [
            "歌舞伎町大乱闘はなぜ起きた？無関係のスカウトまで巻き込んだか - livedoor",
            "小惑星アポフィスの軌道変化を検出、2068年の衝突リスクに影響？ - sorae 宇宙へのポータルサイト",
            "SNSでメッセージを送ってくる男性心理とは？ - livedoor",
          ],
        },
        {
          id: 5,
          title: "スポーツ",
          examples: [
            '阪神・藤川、球団に"残留" 新ポスト「スペシャルアシスタント」就任（サンケイスポーツ） - スポーツナビ',
            "J2新潟社長の引責辞任で問われる棚上げ状態のJ1仙台責任問題（THE PAGE） - Yahoo!ニュース",
            "ダニール・クビアト 「ルクレールを信頼していたからアウトから抜けた」 / アルファタウリ・ホンダF1 - F1-Gate.com",
          ],
        },
        {
          id: 6,
          title: "テクノロジー",
          examples: [
            "コロナ禍で「Amazonの偽レビュー」が全体の42％に達したという報告 - GIGAZINE",
            "iOS14.2で使える絵文字増えたけど...「ゴキブリ」追加で悲鳴が 「奴がいるから一生アップデートできない」（J-CASTニュース） - Yahoo!ニュース",
            "楽天モバイル「月額2980円」、他社も値下げで優位性なし…通信無制限のまやかし - Business Journal",
          ],
        },
        {
          id: 7,
          title: "ビジネス",
          examples: [
            "Ryzen 9 5900Xを早速購入、Ryzen 9 3900を大幅に上回る性能を体感してみた - AKIBA PC Hotline!",
            "米国株、ダウ反落し66ドル安 利益確定の売り優勢 ナスダックは2カ月ぶり高値 - 日本経済新聞",
            "調布市の道路が陥没した問題で説明会 住民から怒りの声 - livedoor",
          ],
        },
        {
          id: 8,
          title: "Thank You！",
          examples: [
            "あなたが興味のある話題を提供する準備が整いました！",
          ],
        },
      ],
    };
  },
  computed: {
    current() {
      return this.list.find((el) => el.id === this.currentId) || {};
    },
  },
};
</script>

<style scoped>
.fav-btn {
  width: 30%;
}
#fav {
  margin-left: 2rem;
}
#unfav {
  margin-right: 2rem;
  color: #0060aa;
}
.paging {
  width: 3rem;
  height: 3rem;
}
#back {
  margin-right: 6rem;
}
#prog {
  margin-left: 6rem;
}
#progress {
  color: #ffa200;
}
</style>

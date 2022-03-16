<template>
  <div class="app-probility-display-container">
    <div class="title">概率显示</div>
    <!-- 概率条 -->
    <div class="probility-display-container">
      <div class="probility-list">
        <!-- FOR -->
        <div v-for="item in probility" :key="item" class="probility-item">
          <div id="name">{{ item.name }}</div>
          <el-progress :percentage="item.value.toFixed(2)" :format="format" />
          <!-- <div class="probility-value">{{ item.value.toFixed(2) }}%</div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import DataProgress from "./progress/DataProgress.vue";
export default {
  name: "ProbilityDisplay",
  components: {},
  data() {
    return {
      title: "Hello Vue!",
    };
  },
  props: {
    prop_probility: {
      type: Array,
      default() {
        return [
          { name: "class1", value: 10 },
          { name: "class2", value: 20 },
          { name: "class3", value: 30 },
          { name: "class4", value: 40 },
          { name: "class5", value: 50 },
        ];
      },
    },
  },
  computed: {
    // 计算概率
    probility() {
      var _probility = this.prop_probility;
      var sum = 0;
      for (var i = 0; i < _probility.length; i++) {
        sum += _probility[i].value;
      }
      for (let i = 0; i < _probility.length; i++) {
        var value = _probility[i].value;
        value = (value / sum) * 100;
        _probility[i].value = value;
      }
      console.log(_probility);
      return _probility;
    },
  },
};
</script>

<style>
/* probility-item */
.probility-item {
  list-style: none;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}
/* .progress {
  height: 3rem;
} */
/* .probility-name {
  width: 5rem;
} */
/* .progress-container {
  width: 100%;
  padding-left: 5px;
  padding-right: 5px;
} */
/* .probility-value {
  width: 5rem;
  font-size: 0.8rem;
} */
</style>

<style>
.el-progress--line {
  margin-bottom: 15px;
  width: 350px;
}
</style>
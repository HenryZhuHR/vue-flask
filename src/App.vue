<template>
  <div class="mainpage">
    <div class="header">
      <GlobalHeader title="深度学习" />
    </div>
    <div class="container">
      <AppPartseg />
    </div>

    <div class="probability-display">
      <ProbabilityDisplay />
    </div>
  </div>
</template>

<script>
import GlobalHeader from "./components/GlobalHeader.vue";
import AppPartseg from "./components/AppPartseg.vue";
import ProbabilityDisplay from "./components/ProbabilityDisplay.vue";
export default {
  name: "App",
  components: {
    GlobalHeader,
    AppPartseg,
    ProbabilityDisplay, //进度条
  },
  data() {
    return {
      title: "Hello Vue!",
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>

<style>
.mainpage{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.header{
  width: 100%;
  height: 60px;
  background-color: blue;
  text-align: center;
}
</style>

<style>
.probability-display {
  width: 30%;
  background-color: #f5f5f5;
}
</style>

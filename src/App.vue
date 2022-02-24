<template>
  <div><GlobalHeader title="深度学习" /></div>
  <div class="container">
    <AppPartseg />
  </div>
</template>

<script>
import GlobalHeader from "./components/GlobalHeader.vue";
import AppPartseg from "./components/AppPartseg.vue";
export default {
  name: "App",
  components: {
    GlobalHeader,
    AppPartseg,
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
  margin-top: 60px;
}
</style>

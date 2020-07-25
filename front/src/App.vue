<template>
  <v-app id="app">
    <router-view></router-view>
    <ScrollTop />
  </v-app>
</template>

<script>
import ScrollTop from "./components/others/layouts/ScrollTop";

export default {
  name: "app",
  components: {
    ScrollTop
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style>
div[class^=col] {
  padding: 0px !important;
}
</style>

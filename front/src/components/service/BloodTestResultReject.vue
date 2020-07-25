<template>
  <div class="note-box do-not-box">
    <div class="note-box-header">
      <div class="icon-element">
        <vue-icon name="x"></vue-icon>
      </div>
      <h3 class="widget-title note-title text-uppercase">{{ title }}</h3>
    </div>
    <div class="section-block"></div>
  </div>
</template>

<script>
export default {
  name: "ServiceTwoLeft",
  props: {
    user: Object,
  },
  data() {
    return {
      title: "가입거절 대상입니다.",
    };
  },
};
</script>

<style scoped>
.v-application a {
  color: white !important;
}
</style>

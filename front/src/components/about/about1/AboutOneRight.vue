<template>
  <div class="service-item">
    <div class="video-popup" :class="{ active: isVisiblePopup }">
      <div class="video-popup-bg" v-on:click="showVideo"></div>
      <div class="video-popup-wrap">
        <span class="close-btn" v-on:click="showVideo">
          <v-icon name="x"></v-icon>
        </span>
      </div>
    </div>
    <img src="../../../assets/images/img1.jpg" alt="About" />
  </div>
</template>

<script>
export default {
  name: "AboutOneRight",
  data() {
    return {
      buttonText: "Video Guideline",
      isVisiblePopup: false,
    };
  },
};
</script>

<style scoped></style>

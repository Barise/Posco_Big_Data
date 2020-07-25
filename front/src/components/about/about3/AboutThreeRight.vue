<template>
  <div class="service-item">
    <div class="video-popup" :class="{active: isVisiblePopup}">
      <div class="video-popup-bg" v-on:click="showVideo"></div>
      <div class="video-popup-wrap">
        <span class="close-btn" v-on:click="showVideo">
          <v-icon name="x"></v-icon>
        </span>
        <iframe src="https://www.youtube.com/embed/X31g5TB-MRo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen ></iframe>
      </div>
    </div>

    <img src="../../../assets/images/img2.jpg" alt="About">
    <div class="service-item-video">
      <span> {{buttonText}}</span>
      <a v-on:click="showVideo" class="video-btn video-play-btn" href="#" title="Watch Video">
        <v-icon name="play"></v-icon>
      </a>
    </div>
  </div>
</template>

<script>
    export default {
        name: "AboutThreeRight",
      data() {
        return {
          buttonText: 'Video Guideline',
          isVisiblePopup: false
        }
      },
      methods: {
        showVideo: function (e) {
          e.preventDefault();
          this.isVisiblePopup = !this.isVisiblePopup;
        }
      }
    }
</script>

<style scoped>

</style>

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


    <img :src="img" alt="About">
    <div class="service-item-video service-item-video-2">
      <a class="mfp-iframe video-btn video-play-btn"
         v-on:click="showVideo" href="#" title="Watch Video">
        <v-icon name="play"></v-icon>
      </a>
      <span> {{buttonText}}</span>
    </div>
  </div>
</template>

<script>
    export default {
      name: "AboutSixLeft",
      data() {
        return {
          isVisiblePopup: false,
          img: require('@/assets/images/img2.jpg'),
          buttonText: 'Video Guideline'
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

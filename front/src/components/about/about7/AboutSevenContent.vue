<template>
  <div class="service-item corona-detail-wrap">
    <div class="corona-img">
      <img :src="img" alt="About">
    </div>
    <div class="corona-detail">
      <ul class="list-items mb-3">
        <li v-for="(list, index) in lists" v-bind:key="index">{{list}}</li>
      </ul>
      <div class="section-block"></div>
      <p class="pt-3">{{caption}}</p>
    </div>
  </div>
</template>

<script>
    export default {
      name: "AboutSevenContent",
      data() {
        return {
          img: require('@/assets/images/corona-virus.jpg'),
          caption: 'Source: World Health Organization',
          lists: [
            "'CO' Stands for corona",
            "'VI' for Virus",
            "'D' for Disease",
            "'19' for 2019 - the year it was first identified"
          ]
        }
      }
    }
</script>

<style scoped>

</style>

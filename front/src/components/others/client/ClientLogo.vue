<template>
  <div class="client-logo-wrap d-flex flex-wrap justify-content-center align-items-center">

    <div class="client-logo-item" v-for="(image, index) in images" v-bind:key="index">
      <img :src="image" class="img-fluid" alt="brand-image">
    </div>

  </div>
</template>

<script>
    export default {
      name: "ClientLogo",
      data() {
        return {
          images: [
            require("@/assets/images/client-logo.png"),
            require("@/assets/images/client-logo-2.png"),
            require("@/assets/images/client-logo-3.png"),
            require("@/assets/images/client-logo-4.png"),
            require("@/assets/images/client-logo-5.png"),
            require("@/assets/images/client-logo-6.png"),
            require("@/assets/images/client-logo-7.png"),
            require("@/assets/images/client-logo-8.png"),
            require("@/assets/images/client-logo-9.png"),
            require("@/assets/images/client-logo-10.png"),
            require("@/assets/images/client-logo-11.png"),
            require("@/assets/images/client-logo-3.png"),
            require("@/assets/images/client-logo-4.png"),
            require("@/assets/images/client-logo-5.png"),
          ]
        }
      }
    }
</script>

<style scoped>

</style>

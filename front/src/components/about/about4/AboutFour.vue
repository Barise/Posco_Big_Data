<template>
  <div class="row">
    <div class="col-lg-5">
      <AboutFourLeft />
    </div>
    <div class="col-lg-6 ml-auto">
      <AboutFourRight />
    </div>
  </div>
</template>

<script>
    import AboutFourLeft from "./AboutFourLeft";
    import AboutFourRight from "./AboutFourRight";
    export default {
      name: "AboutFour",
      components: {
        AboutFourRight,
        AboutFourLeft
      }
    }
</script>

<style scoped>

</style>

<template>
  <div class="row padding-top-90px align-items-center">
    <div class="col-lg-6">
      <AboutSixLeft />
    </div>
    <div class="col-lg-6">
      <AboutSixRgiht />
    </div>
  </div>
</template>

<script>
    import AboutSixLeft from "./AboutSixLeft";
    import AboutSixRgiht from "./AboutSixRgiht";
    export default {
      name: "AboutSix",
      components: {AboutSixRgiht, AboutSixLeft},
    }
</script>

<style scoped>

</style>

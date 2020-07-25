<template>
  <div class="row padding-top-90px align-items-center">
    <div class="col-lg-6">
      <AboutThreeLeft/>
    </div>
    <div class="col-lg-6">
      <AboutThreeRight/>
    </div>
  </div>
</template>

<script>
  import AboutThreeLeft from "./AboutThreeLeft";
  import AboutThreeRight from "./AboutThreeRight";


    export default {
      name: "AboutThree",
      components: {
        AboutThreeLeft,
        AboutThreeRight
      }
    }
</script>

<style scoped>

</style>

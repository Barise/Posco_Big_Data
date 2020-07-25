<template>
      <div class="row padding-top-90px align-items-center">
        <div class="col-lg-6">
          <AboutTwoLeft/>
        </div>
        <div class="col-lg-6">
          <AboutTwoRight/>
        </div>
      </div>
</template>

<script>
  import AboutTwoLeft from "./AboutTwoLeft";
  import AboutTwoRight from "./AboutTwoRight";


    export default {
      name: "AboutTwo",
      components: {
        AboutTwoLeft,
        AboutTwoRight
      }
    }
</script>

<style scoped>

</style>

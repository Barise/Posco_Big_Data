<template>
  <div class="row">
    <div class="col-lg-6">
      <AboutFiveLeftCompany />
    </div>
    <div class="col-lg-6">
      <AboutFiveRightCompany />
    </div>
  </div>
</template>

<script>
import AboutFiveLeftCompany from "./AboutFiveLeftCompany";
import AboutFiveRightCompany from "./AboutFiveRightCompany";
export default {
  name: "AboutFive",
  components: { AboutFiveRightCompany, AboutFiveLeftCompany },
};
</script>

<style scoped></style>

<template>
  <div class="row mt-5">
    <div class="col-lg-7">
      <Accordion />
    </div>
    <div class="col-lg-5">
      <GetInTouch stitle="get in touch" title="Still Have Question? Contact with" />
    </div>
  </div>
</template>

<script>
    import Accordion from "./Accordion";
    import GetInTouch from "../../contact/forms/GetInTouch";
    export default {
        name: "Faq",
      components: {GetInTouch, Accordion}
    }
</script>

<style scoped>
div[class^=col] {
  padding: 12px !important;
}
</style>

<template>
  <section class="slider-area banner-area-2 text-center">
    <div class="single-slide-item banner-item-3">
      <div id="particles-bg-2"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="banner-content">
              <div class="section-heading" style>
                <img src="../../../assets/images/Page_logo.png" alt="포빅 생명 기업용 페이지" />
              </div>
            </div>
          </div>
        </div>

        <!-- Fun Facts -->
        <FunFacts />
      </div>
    </div>
  </section>
</template>

<script>
import FunFacts from "../../others/funfact/FunFacts";
export default {
  name: "CompanyBanner",
  components: {
    FunFacts,
  },
  data() {
    return {
      title: "We Create Insurnace ‘FOR BIG’ Happinies",
    };
  },
};
</script>

<style scoped></style>

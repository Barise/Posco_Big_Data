<template>
  <div class="section-content-box pl-5">
    <SectionTitle
      stitle="More Information About (For Big)"
      title="고객님만을 위한 추천 상품을 알고싶다면?"
      children=""
    />
    <h4 class="widget-title pt-4 pb-3"></h4>
    <div class="section-description">
      <p class="section__desc mb-2">
        <!-- Morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        Vestibulum tortor quam, -->
      </p>
    </div>
    <div class="btn-box">
      <router-link to="/customer/recommend" class="template-btn">{{
        buttonText
      }}</router-link>
    </div>
  </div>
</template>

<script>
import SectionTitle from "../../common/SectionTitle";
export default {
  name: "AboutFiveRight",
  components: {
    SectionTitle,
  },
  data() {
    return {
      buttonText: "일반 심사 페이지로 이동",
    };
  },
};
</script>

<style scoped>
.v-application a {
  color: white !important;
}
</style>

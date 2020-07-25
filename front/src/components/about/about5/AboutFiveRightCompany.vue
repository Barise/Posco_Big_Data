<template>
  <div class="section-content-box pl-5">
    <SectionTitleCompany
      stitle="More Information About (For Big)"
      title="포빅 생명의 금주 일정"
      children="Coronavirus disease is an infectious disease caused by a new virus"
    />
    <h4
      class="widget-title pt-4 pb-3"
    >Coronavirus disease is an infectious disease caused by a new virus</h4>
    <div class="section-description">
      <p class="section__desc mb-2">
        Morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        Vestibulum tortor quam, feugiat vitae, tristique senectus et netus et
        malesuada fames ac turpis
      </p>
      <p class="section__desc">
        Distinctiv enable adaptive niche markets without principle-centered
        sourcesn Collaborati develop impactful expertise and enabled materials
        awesome and Efficiently engineer alternative growth strategies.
      </p>
    </div>
    <div class="btn-box">
      <router-link to="/company/manage" class="template-btn">
        {{
        buttonText
        }}
      </router-link>
    </div>
  </div>
</template>

<script>
import SectionTitleCompany from "../../common/SectionTitleCompany";
export default {
  name: "AboutFiveRightCompany",
  components: {
    SectionTitleCompany,
  },
  data() {
    return {
      buttonText: "고객관리 페이지 이동",
    };
  },
};
</script>

<style scoped></style>

<template>
  <div class="about-item-box text-left">
    <SectionTitle title="Know More About Coronavirus (COVID-19)" stitle="More Information About (COVID-2019)" />
    <div class="section-description padding-top-20px">
      <p class="section__desc">
        {{desc}}
      </p>
    </div>
    <AboutFourIconList />
  </div>
</template>

<script>
    import AboutFourIconList from "./AboutFourIconList";
    import SectionTitle from "../../common/SectionTitle";
    export default {
      name: "AboutFourLeft",
      components: {
        SectionTitle,
        AboutFourIconList
      },
      data() {
        return {
          desc: 'Morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, tristique senectus et netus et malesuada fames ac turpis'
        }
      }
    }
</script>

<style scoped>

</style>

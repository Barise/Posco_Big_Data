<template>
  <main class="home-1">
    <CompanyNavbar />
    <!-- Slider -->
    <CompanyBanner />

    <!-- About Five -->
    <section class="about-area about5 before-after-none section-padding">
      <div class="container">
        <AboutFiveCompany />
      </div>
    </section>
    <divider />
    <!-- CTA -->
    <section class="subscriber-area padding-top-80px padding-bottom-80px">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-7">
            <SectionTitle
              stitle="newsletter"
              title="Subscribe Our Newsletter to get Insurances Updates"
            />
          </div>
          <div class="col-lg-5">
            <MailChimp />
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <Footer />
  </main>
</template>

<script>
import SectionTitle from "../components/common/SectionTitle";
import Divider from "../components/common/Divider";
import AboutFiveCompany from "../components/about/about5/AboutFiveCompany";
import MailChimp from "../components/others/mailchimp/MailChimp";
import CompanyNavbar from "../components/common/CompanyNavbar";
import Footer from "../components/common/footer/Footer";
import CompanyBanner from "../components/banners/banner2/CompanyBanner";
export default {
  name: "Home",
  components: {
    Footer,
    CompanyNavbar,
    MailChimp,
    AboutFiveCompany,
    Divider,
    SectionTitle,
    // HeroSlider,
    CompanyBanner,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.funfact-area .section-heading,
.about-area .section-heading {
  max-width: 700px;
  margin: auto;
}
.blog-area .section-heading {
  max-width: 400px;
  margin: auto;
}
.service2 .section-heading {
  max-width: 500px;
  margin: auto;
}
.about-area {
  z-index: 9;
}
.about2 {
  z-index: 8;
}
.about5 {
  z-index: 7;
}
</style>

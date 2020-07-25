<template>
  <main class="home-1">
    <CustomerNavbar />
    <!-- Slider -->
    <CustomerBanner />

    <divider />
    <!-- Main Page => 고객추천 -->
    <section class="about-area about5 before-after-none section-padding">
      <div class="container">
        <AboutFive />
      </div>
    </section>

    <divider />

    <!-- FAQ -->
    <section class="accordion-area section-bg section-padding">
      <div class="container">
        <div class="row text-center">
          <SectionTitle
            stitle="자주하는 질문(FAQ)"
            title="Looking For An Answer?"
          />
        </div>
        <Faq />
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
              title="Subscribe Our Newsletter to get Coronavirus Updates"
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
import AboutFive from "../components/about/about5/AboutFive";
import Faq from "../components/others/faq/Faq";
import MailChimp from "../components/others/mailchimp/MailChimp";
import CustomerNavbar from "../components/common/CustomerNavbar";
import Footer from "../components/common/footer/Footer";
import CustomerBanner from "../components/banners/banner2/CustomerBanner";
export default {
  name: "CustomerHome",
  components: {
    Footer,
    CustomerNavbar,
    MailChimp,
    Faq,
    AboutFive,
    Divider,
    SectionTitle,
    CustomerBanner,
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

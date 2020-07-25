<template>
  <main class="faq">
    <!--Navbar-->
    <CompanyNavbar />

    <!--CompanyBreadcrumb-->
    <CompanyBreadcrumb title="Faqs" />

    <!-- FAQ -->
    <section class="accordion-area section-padding">
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

    <!-- Footer -->
    <Footer />
  </main>
</template>

<script>
import CompanyNavbar from "../../components/common/CompanyNavbar";
import CompanyBreadcrumb from "../../components/common/CompanyBreadcrumb";
import Faq from "../../components/others/faq/Faq";
import SectionTitle from "../../components/common/SectionTitle";
import Footer from "../../components/common/footer/Footer";
export default {
  name: "FAQ",
  components: {
    Footer,
    SectionTitle,
    Faq,
    CompanyBreadcrumb,
    CompanyNavbar,
  },
};
</script>

<style scoped></style>

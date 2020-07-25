<template>
  <main class="faq">
    <!--Navbar-->
    <CustomerNavbar />

    <!--CustomerBreadcrumb-->
    <CustomerBreadcrumb title="Faqs" />

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
import CustomerNavbar from "../../components/common/CustomerNavbar";
import CustomerBreadcrumb from "../../components/common/CustomerBreadcrumb";
import Faq from "../../components/others/faq/Faq";
import SectionTitle from "../../components/common/SectionTitle";
import Footer from "../../components/common/footer/Footer";
export default {
  name: "FAQ",
  components: {
    Footer,
    SectionTitle,
    Faq,
    CustomerBreadcrumb,
    CustomerNavbar,
  },
};
</script>

<style scoped></style>

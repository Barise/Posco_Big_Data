<template>
  <main class="contact">
    <!-- Navbar -->
    <CompanyNavbar />

    <!-- CompanyBreadcrumb -->
    <CompanyBreadcrumb title="Contact Us" />

    <!-- Contact -->
    <section class="contact-area padding-top-140px padding-bottom-120px">
      <div class="container">
        <ContactWrap />
      </div>
    </section>

    <!-- Map -->
    <GoogleMap />

    <!-- Footer -->
    <Footer />
  </main>
</template>

<script>
import CompanyNavbar from "../../components/common/CompanyNavbar";
import CompanyBreadcrumb from "../../components/common/CompanyBreadcrumb";
import ContactWrap from "../../components/contact/contact/ContactWrap";
import Footer from "../../components/common/footer/Footer";
import GoogleMap from "../../components/contact/maps/GoogleMap";
export default {
  name: "Contact",
  components: {
    GoogleMap,
    Footer,
    ContactWrap,
    CompanyBreadcrumb,
    CompanyNavbar
  }
};
</script>

<style scoped>
</style>
